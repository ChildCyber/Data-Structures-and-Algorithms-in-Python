class Edge:
    """
    Lightweight edge structure for a graph.
    """
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        """
        Do not call constructor directly. Use Graph's insert_edge(u, v, x).
        """
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        """
        边的端点，u为起点，v为终点
        Return (u, v) tuple for vertices u and v.
        """
        return self._origin, self._destination

    def opposite(self, v):
        """
        Return the vertex that is opposite v on this edge.
        """
        return self._destination if v is self._origin else self._origin

    def element(self):
        """
        Return element associated with this edge.
        """
        return self._element

    def __hash__(self):  # will allow edge to be a map/set key
        return hash((self._origin, self._destination))
