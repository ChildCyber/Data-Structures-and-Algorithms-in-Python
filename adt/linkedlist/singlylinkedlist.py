from core.exceptions import Empty
from .node import _SinglyNode as _Node


class LinkedList:

    def __init__(self):
        """
        Create an empty list.
        """
        # reference to the head node
        self._head = _Node(None, None)
        # number of stack elements
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

    def add_first(self, e):
        """
        Add element e at the beginning.
        """
        newest = _Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1
        return newest

    def add_last(self, e):
        """
        Insert element e at the end.
        """
        newest = _Node(e, None)
        if self.is_empty():
            self._head = newest
            self._size += 1
        else:
            cur = self._head
            while cur._next is not None:
                cur = cur._next
            cur._next = newest
            self._size += 1
        return newest

    def remove_first(self):
        """
        remove the node at the beginning.
        """
        if self.is_empty():
            raise Empty('LinkedList is empty')

        node = self._head
        self._head = self._head._next
        self._size -= 1
        element = node._element
        node = None
        return element

    def remove_last(self):
        """
        remove the node at the end.
        """
        if self.is_empty():
            raise Empty('LinkedList is empty')

        node = self._head
        if self._size == 1:
            self._head = _Node(None, None)
            self._size -= 1
            return node._element

        while node._next is not None:
            node = node._next
            if node._next is None:
                tail = node._next
                self._size -= 1
        node._next = None
        element = tail._element
        element = None
        return element

    def search(self, e):
        """
        找出第一个元素为e的节点
        """
        node = self._head
        while node is not None and node._element != e:
            node = node._next
        return node

    def remove_node(self, node):
        if self.is_empty():
            raise Empty('LinkedList is empty')

        if self._size == 1:
            self._head = _Node(None, None)
            self._size -= 1
        else:
            if node._next is None:
                self.remove_last()
            else:
                nxt = node._next
                node._element = nxt._element
                node._next = nxt._next
                nxt = None
                self._size -= 1
        return node._element

    def remove_element(self, e):
        pass
