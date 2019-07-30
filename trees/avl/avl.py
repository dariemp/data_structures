from node import Node

class AVL(object):

    def __init__(self):
        self._root = None

    @property
    def root_key(self):
        if self._root:
            return self._root.key
        return None

    @property
    def root_data(self):
        if self._root:
            return self._root.data
        return None

    @property
    def height(self):
        return self._get_height(self._root)

    def insert(self, key, data):
        self._root = self._search_and_insert(self._root, key, data)

    def in_order(self, recorder_method, on_data=False):
        self._in_order(self._root, recorder_method, on_data)

    def range(self, recorder_method, first_key, last_key, on_data=False):
        if first_key >= last_key:
            raise ValueError('First key must be strictly less than last key')
        self._range(self._root, recorder_method, first_key, last_key, on_data)

    def _search_and_insert(self, node, key, data):
        if not node:
            return Node(key, data)
        node = self._search_and_insert_in_children(node, key, data)
        self._update_height(node)
        node = self._rebalance(node, key)
        return node

    def _search_and_insert_in_children(self, node, key, data):
        if key < node.key:
            node.left_child = self._search_and_insert(node.left_child, key, data)
        elif key > node.key:
            node.right_child = self._search_and_insert(node.right_child, key, data)
        return node

    def _update_height(self, node):
        node.height = 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _rebalance(self, node, key):
        balance_factor = self._get_balance_factor(node)
        node = self._do_right_rotations_if_needed(balance_factor, node, key)
        node = self._do_left_rotations_if_needed(balance_factor, node, key)
        return node 

    def _get_balance_factor(self, node):
        if not node: 
            return 0
        return self._get_height(node.left_child) - self._get_height(node.right_child)

    def _do_right_rotations_if_needed(self, balance_factor, node, key):
        if balance_factor > 1:
            if key < node.left_child.key: 
                return self._right_rotate(node) 
            elif key > node.left_child.key: 
                node.left_child = self._left_rotate(node.left_child) 
                return self._right_rotate(node)
        return node

    def _do_left_rotations_if_needed(self, balance_factor, node, key):
        if balance_factor < -1:
            if key < node.right_child.key: 
                node.right_child = self._right_rotate(node.right_child) 
                return self._left_rotate(node) 
            elif key > node.right_child.key: 
                return self._left_rotate(node)
        return node

    def _left_rotate(self, node):
        new_root = node.right_child 
        temp_subtree = new_root.left_child

        new_root.left_child = node
        node.right_child = temp_subtree
  
        self._update_height(node)
        self._update_height(new_root)
  
        return new_root

    def _right_rotate(self, node):
        new_root = node.left_child
        temp_subtree = new_root.right_child 
  
        new_root.right_child = node
        node.left_child = temp_subtree
  
        self._update_height(node)
        self._update_height(new_root)
  
        return new_root

    def _in_order(self, node, recorder_method, on_data=False):
        if not node:
            return
        self._in_order(node.left_child, recorder_method, on_data)
        self._record_node_visit(node, recorder_method, on_data)
        self._in_order(node.right_child, recorder_method, on_data)

    def _record_node_visit(self, node, recorder_method, on_data=False):
        value = self._get_value_for_ordering(node, on_data)
        recorder_method(value)

    def _get_value_for_ordering(self, node, on_data=False):
        if on_data:
            value = node.data
        else:
            value = node.key
        return value

    def _range(self, node, recorder_method, first_key, last_key, on_data=False):
        if not node:
           return
        self._range_from_middle_if_in_middle(node, recorder_method, first_key, last_key, on_data)
        self._range_from_left_child_if_range_at_left(node, recorder_method, first_key, last_key, on_data)
        self._range_from_right_child_if_range_at_right(node, recorder_method, first_key, last_key, on_data)

    def _range_from_middle_if_in_middle(self, node, recorder_method, first_key, last_key, on_data=False):
        self._partial_range_from_left_child_if_range_starts_at_left(node, recorder_method, first_key, on_data)
        self._add_current_node_if_in_range(node, recorder_method, first_key, last_key, on_data)
        self._partial_range_from_right_child_if_range_ends_at_right(node, recorder_method, last_key, on_data)

    def _add_current_node_if_in_range(self, node, recorder_method, first_key, last_key, on_data=False):
        if (first_key and first_key <= node.key) or (last_key and node.key <= last_key):
            self._record_node_visit(node, recorder_method, on_data)

    def _range_from_left_child_if_range_at_left(self, node, recorder_method, first_key, last_key, on_data=False):
        if last_key < node.key:
            self._range(node.left_child, recorder_method, first_key, last_key, on_data)

    def _range_from_right_child_if_range_at_right(self, node, recorder_method, first_key, last_key, on_data=False):
        if node.key < first_key:
            self._range(node.right_child, recorder_method, first_key, last_key, on_data)

    def _partial_range_from_left_child_if_range_starts_at_left(self, node, recorder_method, key, on_data=False):
        if key < node.key:
            self._partial_range_from_left_child(node.left_child, recorder_method, key, on_data)

    def _partial_range_from_right_child_if_range_ends_at_right(self, node, recorder_method, key, on_data=False):
        if node.key < key:
            self._partial_range_from_right_child(node.right_child, recorder_method, key, on_data)

    def _partial_range_from_left_child(self, node, recorder_method, first_key, on_data=False):
        if not node:
           return
        self._partial_range_from_left_child_if_range_starts_at_left(node, recorder_method, first_key, on_data)
        self._add_current_node_if_in_range(node, recorder_method, first_key, None, on_data)
        self._partial_range_from_left_child(node.right_child, recorder_method, first_key, on_data)

    def _partial_range_from_right_child(self, node, recorder_method, last_key, on_data=False):
        if not node:
           return
        self._partial_range_from_right_child(node.left_child, recorder_method, last_key, on_data)
        self._add_current_node_if_in_range(node, recorder_method, None, last_key, on_data)
        self._partial_range_from_right_child_if_range_ends_at_right(node, recorder_method, last_key, on_data)
