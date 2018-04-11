import ctypes


class DynamicArray:
    """
    A dynamic array class akin to a simplified Python list.
    """

    def __init__(self):
        """
        Create an empty array.
        """
        # count actual elements
        self._n = 0
        # default array capacity
        self._capacity = 1
        # low-level array
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """
        Return number of elements stored in the array.
        """
        return self._n

    def __getitem__(self, k):
        """
        Return element at index k.
        """
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        # retrieve from array
        return self._A[k]

    def append(self, obj):
        """
        Add object to end of the array.
        """
        # not enough room
        if self._n == self._capacity:
            # so double capacity
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """
        Resize internal array to capacity c.
        """
        # new(bigger) array
        bigger = self._make_array(c)
        # for each existing value
        for k in range(self._n):
            bigger[k] = self._A[k]
        # use the bigger array
        self._A = bigger
        self._capacity = c

    def _make_array(self, c):
        """
        Return new array with capacity c.
        """
        # see ctypes documentation
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        """
        Insert value at index k, shifting subsequent values rightward.
        """
        # (for simplicity, we assume 0 <= k <= n in this version)
        # not enough room
        if self._n == self._capacity:
            # so double capacity
            self._resize(2 * self._capacity)
        # shift rightmost first
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        # store newest element
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """
        Remove first occurrence of value (or raise ValueError).
        """
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            # found a match!
            if self._A[k] == value:
                # shift others to fill gap
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                # help garbage collection
                self._A[self._n - 1] = None
                # we have one less item
                self._n -= 1
                # exit immediately
                return
        # only reached if no match
        raise ValueError('value not found')
