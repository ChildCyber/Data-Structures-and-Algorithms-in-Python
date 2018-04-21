from .map import MapBase


class SortedTableMap(MapBase):
    """
    Map implementation using a sorted table.
    """

    # nonpublic behaviors
    def _find_index(self, k, low, high):
        """
        Return index of the leftmost item with key greater than or equal to k.
        Return high + 1 if no such item qualifies.
        That is, j will be returned such that:
            all items of slice table[low:j] have key < k
            all items of slice table[j:high+1] have key >= k
        """
        if high < low:
            # no element qualifies
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                # found exact match
                return mid
            elif k < self._table[mid]._key:
                # note: may return mid
                return self._find_index(k, low, mid - 1)
            else:
                # answer is right of mid
                return self._find_index(k, mid + 1, high)

    # public behaviors
    def __init__(self):
        """
        Create an empty map.
        """
        self._table = []

    def __len__(self):
        """
        Return number of items in the map.
        """
        return len(self._table)

    def __getitem__(self, k):
        """
        Return value associated with key k (raise KeyError if not found).
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error:' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        """
        Assign value v to key k, overwriting existing value if present.
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            # reassign value
            self._table[j]._value = v
        else:
            # adds new item
            self._table.insert(j, self._Item(k, v))

    def __delitem__(self, k):
        """
        Remove item associated with key k (raise KeyError if not found).
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        # delete item
        self._table.pop(j)

    def __iter__(self):
        """
        Generate keys of the map ordered from minimum to maximum.
        """
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """
        Generate keys of the map ordered from maximum to minimum.
        """
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """
        Return (key, value) pair with minimum key (or None if empty).
        """
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """
        Return (key, value) pair with maximum key (or None if empty).
        """
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """
        Return (key, value) pair with least key greater than or equal to k.
        """
        # j's key >= k
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_lt(self, k):
        """
        Return (key, value) pair with greatest key strictly less than k.
        """
        # j's key >= k
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            # note use of j-1
            return (self._table[j - 1]._key, self._table[j - 1]._value)
        else:
            return None

    def find_gt(self, k):
        """
        Return (key, value) pair with least key strictly greater than k.
        """
        # j's key >= k
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            # advanced past match
            j += 1
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_range(self, start, stop):
        """
        Iterate all (key, value) pairs such that start <= key <= stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if start is None:
            j = 0
        else:
            # find first result
            j = self._find_index(start, 0, len(self._table) - 1)
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1
