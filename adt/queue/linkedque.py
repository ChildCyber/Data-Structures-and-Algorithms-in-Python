from core.exceptions import Empty
from linkedlist.node import _SinglyNode as _Node


class LinkedQueue:
    """
    FIFO queue implementation using a singly linked list for storage.
    """

    def __init__(self):
        """
        Create an empty queue.
        """
        self._head = None
        self._tail = None
        # number of queue elements
        self._size = 0

    def __len__(self):
        """
        Return the number of elements in the queue.
        """
        return self._size

    def is_empty(self):
        """
        Return True if the queue is empty.
        """
        return self._size == 0

    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        # front aligned with head of list
        return self._head._element

    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        # special case as queue is empty
        if self.is_empty():
            # removed head had been the tail
            self._tail = None
        return answer

    def enqueue(self, e):
        """
        Add an element to the back of queue.
        """
        # node will be new tail node
        newest = _Node(e, None)
        if self.is_empty():
            # special case: previously empty
            self._head = newest
        else:
            self._tail._next = newest
        # update reference to tail node
        self._tail = newest
        self._size += 1
