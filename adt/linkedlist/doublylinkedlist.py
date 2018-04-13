from .node import _DoublyNode as _Node


class _DoublyLinkedBase:
    """
    A base class providing a doubly linked list representation.
    """
    def __init__(self):
        """
        Create an empty list.
        """
        self._header = _Node(None, None, None)
        self._trailer = _Node(None, None, None)
        # trailer is after header
        self._header._next = self._trailer
        # header is before trailer
        self._trailer._prev = self._header
        # number of elements
        self._size = 0

    def __len__(self):
        """
        Return the number of elements in the list.
        """
        return self._size

    def is_empty(self):
        """
        Return True if list is empty.
        """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """
        Add element e between two existing nodes and return new node.
        """
        # linked to neighbors
        newest = _Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """
        Delete nonsentinel node from the list and return its element.
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        # record deleted element
        element = node._element
        # deprecate node
        node._prev = node._next = node._element = None
        return element
