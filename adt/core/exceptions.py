class Empty(Exception):
    """
    Error attempting to access an element from an empty container
    """
    pass


class PrioQueueError(ValueError):
    pass


class GraphError(Exception):
    pass
