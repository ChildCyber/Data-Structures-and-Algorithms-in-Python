from .hashmap import HashMapBase
from .hashtable import UnsortedTableMap


class ChainHashMap(HashMapBase):
    """
    Hash map implemented with separate chaining for collision resolution.
    """

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            # no match found
            raise KeyError('Key Error: ' + repr(k))
        # may raise KeyError
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            # bucket is new to the table
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        # key was new to the table
        if len(self._table[j]) > oldsize:
            # increase overall map size
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            # no match found
            raise KeyError('Key Error: ' + repr(k))
        # may raise KeyError
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            # a nonempty slot
            if bucket is not None:
                for key in bucket:
                    yield key
