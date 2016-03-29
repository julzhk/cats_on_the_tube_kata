import unittest
from mapping_elements import Node

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


if __name__ == '__main__':
    unittest.main()