import unittest
from mapping_elements import Node, read_datafile, Graph, Station, Owner, Cat

class TestMap(unittest.TestCase):

    def test_simple_create_node(self):
        mapnode = Node(name='Aldgate')
        self.assertEquals(mapnode.name, 'Aldgate')

    def test_simple_create_node_with_id(self):
        mapnode = Node(name='Aldgate',id = 2)
        self.assertEquals(mapnode.name, 'Aldgate')
        self.assertEquals(mapnode.id, 2)

    def test_simple_create_node_with_connections(self):
        mapnode = Node(name='Aldgate',id = 2)
        mapnode.addconnection(156)
        mapnode.addconnection(263)
        self.assertEquals(mapnode.name, 'Aldgate')
        self.assertEquals(mapnode.id, 2)
        self.assertIn(156, mapnode.connections)
        self.assertIn(263, mapnode.connections)

class TestCreateTubeMap(unittest.TestCase):

    def test_read_datafile(self):
        simplefile = 'simple_map_data.csv'
        for i, [node_id, nodename] in enumerate(read_datafile(simplefile), start=1):
            self.assertEquals(int(node_id), i)
            if i == 1:
                self.assertEquals(nodename,'Acton Town')
            if i == 2:
                self.assertEquals(nodename,'Aldgate')
            if i == 5:
                self.assertEquals(nodename,'Alperton')

    def test_create_tube_graph(self):
        tubegraph = Graph()
        tubegraph.readnodefile('simple_map_data.csv')
        self.assertEquals(len(tubegraph.nodes),5)
        self.assertEquals(tubegraph.nodes[1], Node(name='Acton Town',id='1'))
        self.assertEquals(tubegraph.nodes[1], Node(name='Acton Town',id=1))


    def test_create_tube_connections(self):
        tubegraph = Graph()
        tubegraph.readnodefile('simple_map_data.csv')
        tubegraph.readconnections('simple_map_connections.csv')
        self.assertIn(3,tubegraph.nodes[1].connections)
        self.assertIn(4,tubegraph.nodes[1].connections)
        self.assertTrue(len(tubegraph.nodes[1].connections),2)

class TestOccupiedStatus(unittest.TestCase):

    def test_simple_add_occupiers(self):
        mapnode = Node(name='Aldgate',id = 2)
        mapnode.occupiers = Station()
        mapnode.occupiers.addowner(1)
        mapnode.occupiers.addowner(2)
        mapnode.occupiers.addcat(3)
        self.assertEquals(len(mapnode.occupiers.owners), 2)
        self.assertEquals(len(mapnode.occupiers.cats), 1)

    def test_simple_cat_found(self):
        mapnode = Node(name='Aldgate',id = 2)
        self.assertEquals(mapnode.occupiers.closed, False)
        mapnode.occupiers.addowner(1)
        mapnode.occupiers.addowner(2)
        mapnode.occupiers.addcat(1)
        self.assertEquals(len(mapnode.occupiers.owners), 1)
        self.assertEquals(len(mapnode.occupiers.cats), 0)
        self.assertEquals(mapnode.occupiers.closed, True)
        self.assertEquals('Owner 1 found cat 1 - Aldgate is now closed', mapnode.occupiers.findlog[0])


class TestPlayers(unittest.TestCase):

    def test_create_owners(self):
        owner1 = Owner(id=1)
        self.assertEquals(owner1.id, 1)

    def test_simple_add_occupiers_classes(self):
        mapnode = Node(name='Aldgate',id = 2)
        mapnode.occupiers = Station()

        mapnode.occupiers.addowner(Owner())
        mapnode.occupiers.addowner(Owner())
        mapnode.occupiers.addcat(Cat())
        self.assertEquals(len(mapnode.occupiers.owners), 2)
        self.assertEquals(len(mapnode.occupiers.cats), 1)

if __name__ == '__main__':
    unittest.main()