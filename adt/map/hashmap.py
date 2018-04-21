from random import randrange
from .map import MapBase


class HashMapBase(MapBase):
    """
    Abstract base class for map using hash-table with MAD compression.
    """

    def __init__(self, cap=11, p=109345121):
        """
        Create an empty hash-table map.
        """
        self._table = cap * [None]
        # number of entries in the map
        self._n = 0
        # prime for MAD compression
        self._prime = p
        # scale from 1 to p-1 for MAD
        self._scale = 1 + randrange(p - 1)
        # shift from 0 to p-1 for MAD
        self._shift = randrange(p)

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        # may raise KeyError
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        # subroutine maintains self._n
        self._bucket_setitem(j, k, v)
        # keep load factor <= 0.5
        if self._n > len(self._table) // 2:
            # number 2^x - 1 is often prime
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        # may raise KeyError
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        # resize bucket array to capacity c
        # use iteration to record existing items
        old = list(self.items())
        # then reset table to desired capacity
        self._table = c * [None]
        # n recomputed during subsequent adds
        self._n = 0
        for (k, v) in old:
            # reinsert old key-value pair
            self[k] = v

    # _bucket_getitem, _bucket_setitem, _bucket_delitem 交由子类实现
