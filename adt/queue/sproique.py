from core.exceptions import Empty
from linkedlist.poslist import PositionalList
from .proique import PriorityQueueBase


class SortedPriorityQueue(PriorityQueueBase):
    """
    A min-oriented priority queue implemented with an sorted list.
    """

    def __init__(self):
        """
        Create a new empty Priority Queue.
        """
        self._data = PositionalList()

    def __len__(self):
        """
        Return the number of items in the priority queue.
        """
        return len(self._data)

    def add(self, key, value):
        """
        Add a key-value pair.
        """
        # make new item instance
        newest = self._Item(key, value)
        # walk backward looking for smaller key
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            # new key is smallest
            self._data.add_first(newest)
        else:
            # newest goes after walk
            self._data.add_after(walk, newest)

    def min(self):
        """
        Return but do not remove (k, v) tuple with minimum key.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        """
        Remove and return (k, v) tuple with minimum key.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return item._key, item._value
