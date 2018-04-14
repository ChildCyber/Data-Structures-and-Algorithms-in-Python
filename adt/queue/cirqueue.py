from core.exceptions import Empty
from linkedlist.node import _SinglyNode as _Node


class CircularQueue:
    """
    Queue implementation using circularly linked list for storage.
    """

    def __init__(self):
        """
        Create an empty queue.
        """
        # will represent tail of queue
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
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        # removing only element
        if self._size == 1:
            # queue becomes empty
            self._tail = None
        else:
            # bypass the old head
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._next

    def enqueue(self, e):
        """
        Add an element to the back of queue.
        """
        # node will be new tail node
        newest = _Node(e, None)
        if self.is_empty():
            # initialize circularly
            newest._next = newest
        else:
            # new node points to head
            newest._next = self._tail._next
            # old tail points to new node
            self._tail._next = newest
        # new node becomes the tail
        self._tail = newest
        self._size += 1

    def rotate(self):
        """
        Rotate front element to the back of the queue.
        """
        if self._size > 0:
            # old head becomes new tail
            self._tail = self._tail._next
