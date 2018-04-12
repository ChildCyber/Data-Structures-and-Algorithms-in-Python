from core.exceptions import Empty


class ArrayStack:
    """
    LIFO Stack implementation using a Python list as underlying storage.
    """

    def __init__(self):
        """
        Create an empty stack.
        """
        self._data = []

    def __len__(self):
        """
        Return the number of elements in stack.
        """
        return len(self._data)

    def is_empty(self):
        """
        Return True if the stack is empty.
        """
        return len(self._data) == 0

    def push(self, e):
        """
        Add element e to the top of the stack.
        """
        # new item store at the end of list
        self._data.append(e)

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        # the last item in the list
        return self._data[-1]

    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        # remove last item from list
        return self._data.pop()
