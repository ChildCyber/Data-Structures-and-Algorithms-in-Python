from collections import MutableMapping


class MapBase(MutableMapping):
    """
    Our own abstract base class that includes a nonpublic _Item class.
    """

    class _Item:
        """
        Lightweight composite to store key-value pairs as map items.
        """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            # compare items based on their keys
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            # compare items based on their keys
            return self._key < other._key
