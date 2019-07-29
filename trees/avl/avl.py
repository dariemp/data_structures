from enum import Enum
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

    def in_order(self, accumulator, operator, on_data=False):
        self._in_order(self._root, accumulator, operator, on_data)
        return accumulator

    def _in_order(self, node, accumulator, operator, on_data=False):
        if not node:
            return accumulator
        self._in_order(node.left_child, accumulator, operator, on_data)
        value = self._get_value_for_ordering(node, on_data)
        getattr(accumulator, operator)(value)
        self._in_order(node.right_child, accumulator, operator, on_data)

    def _get_value_for_ordering(self, node, on_data=False):
        if on_data:
            value = node.data
        else:
            value = node.key
        return value
