from .edge import Edge
from .vertex import Vertex


class Graph:
    """
    Representation of a simple graph using an adjacency map.
    """

    def __init__(self, directed: bool = False):
        """
        Create an empty graph (undirected, by default)
        Graph is directed is optional parameter is set to True
        """
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing

    def is_directed(self) -> bool:
        """
        Return True if this is a directed graph; False if undirected.
        Property is based on the original declaration of graph, not its contents.
        """
        return self._incoming is not self._outgoing  # directed if maps is distinct

    def vertex_count(self) -> int:
        """
        Return the number of vertices in the graph.
        """
        return len(self._outgoing)

    def vertices(self):
        """
        Return an iteration of all vertices of the graph.
        """
        return self._outgoing.keys()

    def edge_count(self) -> int:
        """
        Return the number of the edges in the graph.
        """
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2

    def edges(self) -> set:
        """
        Return a set of all edges of the graph.
        """
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u: Vertex, v: Vertex) -> Edge:
        """
        Return the edge from u to v, or None if not adjacent.
        """
        return self._outgoing[u].get(v)  # return None if v not adjacent

    def degree(self, v: Vertex, outgoing: bool = True) -> int:
        """
        Return number of (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to count incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edge(self, v: Vertex, outgoing: bool = True) -> Edge:
        """
        入射边，代表边和顶点之间的关系
        Return all (outgoing) edges incident to vertex in the graph.
        If graph is directed, optional parameter used to request incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None) -> Vertex:
        """
        创建新顶点
        Insert and return a new Vertex with element x.
        """
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # need distinct map for incoming edges
        return v

    def insert_edge(self, u: Vertex, v: Vertex, x=None) -> None:
        """
        创建以u、v为顶点的新边
        Insert and return a new Edge from u to v with auxiliary element x.
        """
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

# Sample
# g = Graph()
# u = g.insert_vertex('u')
# v = g.insert_vertex('v')
# g.insert_edge(u, v, 'e')
