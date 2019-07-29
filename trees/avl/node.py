class Node(object):
    
    def __init__(self, key, data):
        self._key = key
        self._data = data
        self._left_child = None
        self._right_child = None
        self._height = 0

    @property
    def key(self):
        return self._key

    @property
    def data(self):
        return self._data

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, node):
        self._left_child = node

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, node):
        self._right_child = node

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height
