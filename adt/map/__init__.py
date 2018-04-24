from .chainhashmap import ChainHashMap
from .multimap import MultiMap
from .probehashmap import ProbeHashMap
from .shashtable import SortedTableMap
from .hashtable import UnsortedTableMap

__all__ = ['ChainHashMap', 'MultiMap', 'ProbeHashMap', 'SortedTableMap', 'UnsortedTableMap']


def hash_code(s):
    mask = (1 << 32) - 1
    h = 0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(character)
    return h
