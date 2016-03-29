import unittest
from mapping_elements import Node, read_datafile

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
        for i, [node_id, nodename] in enumerate(read_datafile(simplefile),start=1):
            self.assertEquals(int(node_id), i)
            if i == 1:
                self.assertEquals(nodename,'Acton Town')
            if i == 2:
                self.assertEquals(nodename,'Aldgate')
            if i == 5:
                self.assertEquals(nodename,'Alperton')



if __name__ == '__main__':
    unittest.main()