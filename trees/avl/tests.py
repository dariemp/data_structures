import unittest
from avl import AVL

class TestAVL(unittest.TestCase):


    def test_root_key(self):
        keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        avl = self._create_tree_no_data(keys)
        self.assertEqual(avl.root_key, 40)

    def test_height(self):
        keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        avl = self._create_tree_no_data(keys)
        self.assertEqual(avl.height, 4)

    def test_in_order(self):
        keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        expected_result = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        avl = self._create_tree_no_data(keys)
        result = []
        avl.in_order(result, 'append')
        self.assertEqual(expected_result, result)

    def _create_tree_no_data(self, keys):
        avl = AVL()
        for key in keys:
            avl.insert(key, 0)
        return avl
    