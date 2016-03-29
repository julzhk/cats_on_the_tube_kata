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

if __name__ == '__main__':
    unittest.main()