class _SinglyNode:
    """
    Lightweight, nonpublic class for storing a singly linked node.
    """
    # streamline memory usage
    __slots__ = '_element', '_next'

    # initialize node's fields
    def __init__(self, element, next):
        # reference to user's element
        self._element = element
        # reference to next node
        self._next = next


class _DoublyNode:
    """
    Lightweight, nonpublic class for storing a doubly linked node.
    """
    # streamline memory usage
    __slots__ = '_element', '_prev', '_next'

    # initialize node's fields
    def __init__(self, element, prev, next):
        # reference to user's element
        self._element = element
        # previous node reference
        self._prev = prev
        # reference to next node
        self._next = next
