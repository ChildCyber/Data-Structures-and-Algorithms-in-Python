from core.exceptions import GraphError


class Graph:
    """
    邻接矩阵表示法
    """

    def __init__(self, mat, unconn=0):
        """
        :param mat: 矩阵
        :param unconn: 矩阵元素值可以为1或者权值，表示有边，或者使用一个特殊值表示无关联
        """
        vnum = len(mat)
        for x in mat:
            # 检查是否为方阵
            if len(x) != vnum:
                raise ValueError("Argument for 'Graph'.")
        # 拷贝
        self._mat = [mat[i][:] for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        """
        顶点数量
        """
        return self._vnum

    def _invalid(self, v):
        return v < 0 or v >= self._vnum

    def add_vertex(self):
        raise GraphError("Adj-Matrix does not support 'add_vertex'.")

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")
        return self._mat[vi][vj]

    def out_edges(self, vi):
        """
        获取特定顶点的出边
        :param vi: 顶点
        """
        if self._invalid(vi):
            raise GraphError(str(vi) + " is not a valid vertex.")
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    def __str__(self):
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]" + "\nUnconnected: " + str(self._unconn)


class GraphAL(Graph):
    """
    临接表实现
    """

    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        for x in mat:
            # 检查是否为方阵
            if len(x) != vnum:
                raise ValueError("Argument for 'GraphAL'.")

        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        # 增加新顶点时安排一个新编号
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError("Cannot add edge to empty graph.")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) + " is not valid vertex.")

        row = self._mat[vi]
        i = 0
        while i < len(row):
            # 修改mat[vi][vj]的值
            if row[i][0] == vj:
                self._mat[vi][vj] = (vj, val)
                return
            # 原来没有到vj的边，推出循环后加入边
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + " is not a valid vertex.")

        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + " is not a valid vertex.")
        return self._mat[vi]
