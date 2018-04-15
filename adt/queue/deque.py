from core.exceptions import Empty
from linkedlist.doublylinkedlist import _DoublyLinkedBase


class LinkedDeque(_DoublyLinkedBase):
    """
    Double-ended queue implementation based on doubly linked list.
    """

    def first(self):
        """
        Return (but do not remove) the element at the front of the deque.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        # real item just after header
        return self._header._next._element

    def last(self):
        """
        Return (but do not remove) the element at the back of the deque.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        # real item just before trailer
        return self._trailer._prev._element

    def insert_first(self, e):
        """
        Add an element to the front of the deque.
        """
        # after header
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """
        Add an element to the back of the deque.
        """
        # before trailer
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """
        Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        # after header
        if self.is_empty():
            raise Empty('Deque is empty')
        # use inherited method
        return self._delete_node(self._header._next)

    def delete_last(self):
        """
        Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        # after header
        if self.is_empty():
            raise Empty('Deque is empty')
        # use inherited method
        return self._delete_node(self._trailer._prev)
