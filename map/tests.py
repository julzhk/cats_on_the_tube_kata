import unittest
from mapping_elements import Node

class TestMap(unittest.TestCase):

    def test_node(self):
        mapnode = Node(name='Aldgate')
        self.assertEquals(mapnode.name, 'Aldgate')

if __name__ == '__main__':
    unittest.main()