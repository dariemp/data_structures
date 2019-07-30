import unittest
from avl import AVL

class TestAVL(unittest.TestCase):

    def test_root_key(self):
        keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        avl = self._create_tree_no_data(keys)
        self.assertEqual(avl.root_key, 40)

    def test_root_data(self):
        items = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j'}
        avl = self._create_tree_with_data(items)
        self.assertEqual(avl.root_data, 'd')

    def test_height(self):
        keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        avl = self._create_tree_no_data(keys)
        self.assertEqual(avl.height, 4)

    def test_in_order(self):
        keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        expected_result = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        avl = self._create_tree_no_data(keys)
        result = []
        avl.in_order(result.append)
        self.assertEqual(expected_result, result)

    def test_in_order_with_data(self):
        items = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j'}
        expected_result = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        avl = self._create_tree_with_data(items)
        result = []
        avl.in_order(result.append, on_data=True)
        self.assertEqual(expected_result, result)

    def test_in_order_with_data_concatenation(self):
        items = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j'}
        expected_result = 'abcdefghij'
        avl = self._create_tree_with_data(items)
        self.result = ''
        def concat(value):
            self.result += value
        avl.in_order(concat, on_data=True)
        self.assertEqual(expected_result, self.result)

    def test_in_order_with_data_sum(self):
        items = {1:101, 2:102, 3:103, 4:104, 5:105, 6:106, 7:107, 8:108, 9:109, 10:110}
        expected_result = (110 * 111 // 2) - (100 * 101 // 2) 
        avl = self._create_tree_with_data(items)
        self.result = 0
        def xsum(value):
            self.result += value
        avl.in_order(xsum, on_data=True)
        self.assertEqual(expected_result, self.result)

    def test_range_on_empty_avl(self):
        first = 35
        last = 85
        avl = AVL()
        result = []
        avl.range(result.append, first, last)
        self.assertEqual([], result)

    def test_range_35_85(self):
        keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        first = 35
        last = 85
        expected_result = [40, 50, 60, 70, 80]
        avl = self._create_tree_no_data(keys)
        result = []
        avl.range(result.append, first, last)
        self.assertEqual(expected_result, result)

    def test_range_5_70(self):
        keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        first = 5
        last = 70
        expected_result = [10, 20, 30, 40, 50, 60, 70]
        avl = self._create_tree_no_data(keys)
        result = []
        avl.range(result.append, first, last)
        self.assertEqual(expected_result, result)

    def test_range_with_data_concat(self):
        items = {10:'a', 20:'b', 30:'c', 40:'d', 50:'e', 60:'f', 70:'g', 80:'h', 90:'i', 100:'j'}
        first = 15
        last = 70
        expected_result = 'bcdefg'
        avl = self._create_tree_with_data(items)
        self.result = ''
        def concat(value):
            self.result += value
        avl.range(concat, first, last, on_data=True)
        self.assertEqual(expected_result, self.result)

    def _create_tree_no_data(self, keys):
        avl = AVL()
        for key in keys:
            avl.insert(key, 0)
        return avl
    
    def _create_tree_with_data(self, dictionary):
        avl = AVL()
        for key, value in dictionary.items():
            avl.insert(key, value)
        return avl
