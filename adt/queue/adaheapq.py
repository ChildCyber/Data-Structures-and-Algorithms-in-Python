from .heapq import HeapPriorityQueue


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """
    A locator-based priority queue implemented with binary heap.
    """

    class Locator(HeapPriorityQueue._Item):
        """
        Token for locating an entry of the priority queue.
        """
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    # nonpublic behaviors
    # override swap to record new indices
    def _swap(self, i, j):
        # perform the swap
        super()._swap(i, j)
        # reset locator index (post-swap)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._unheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        """
        Add a key-value pair.
        """
        # initialize locator index
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._unheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        """
        Update the key and value for the entry identified by Locator loc.
        """
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        """
        Remove and return the (k, v) pair identified by Locator loc.
        """
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        # item at last position
        if j == len(self) - 1:
            # just remove it
            self._data.pop()
        else:
            # swap item to the last position
            self._swap(j, len(self) - 1)
            # remove it from the list
            self._data.pop()
            # fix item displaced by the swap
            self._bubble(j)

        return loc._key, loc._value
