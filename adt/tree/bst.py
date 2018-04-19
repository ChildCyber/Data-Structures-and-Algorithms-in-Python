from map.map import MapBase
from .lbtree import LinkedBinaryTree


class TreeMap(LinkedBinaryTree, MapBase):
    """
    Sorted map implementation using a binary search tree.
    """

    # override Position class
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """
            Return key of map's key-value pair.
            """
            return self.element()._key

        def value(self):
            """
            Return value of map's key-value pair.
            """
            return self.element()._value

    # nonpublic utilities
    def _subtree_search(self, p: Position, k) -> Position:
        """
        Return Position of p's subtree having key k, or last node searched.
        """
        # found match
        if k == p.key():
            return p
        # search left subtree
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        # search right subtree
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        # unsuccessful search
        return p

    def _subtree_first_position(self, p: Position) -> Position:
        """
        Return Position of first item in subtree rooted at p.
        """
        walk = p
        # keep walking left
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p: Position) -> Position:
        """
        Return Position of last item in subtree rooted at p.
        """
        walk = p
        # keep walking right
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self) -> Position:
        """
        Return the first Position in the tree (or None if empty).
        """
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self) -> Position:
        """
        Return the last Position in the tree (or None if empty).
        """
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p: Position) -> Position:
        """
        Return the Position just before p in the natural order.
        Return None if p is the first position.
        """
        # inherited from LinkedBinaryTree
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p: Position) -> Position:
        """
        Return the Position just after p in the natural order.
        Return None if p is the last position.
        """
        # symmetric to before(p)
        self._validate(p)
        if self.right(p):
            return self._subtree_last_position(self.right(p))
        else:
            # walk upward
            walk = p
            after = self.parent(walk)
            while after is not None and walk == self.right(after):
                walk = after
                after = self.parent(walk)
            return after

    def find_position(self, k) -> Position or None:
        """
        Return position with key k, or else neighbor (or None if empty).
        """
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            # hook for balanced tree subclasses
            self._rebalance_access(p)
            return p

    def find_min(self):
        """
        Return (key, value) pair with minimum key (or None if empty).
        """
        if self.is_empty():
            return None
        else:
            p = self.first()
            return p.key(), p.value()

    def find_ge(self, k):
        """
        Return (key, value) pair with least key greater than or equal to k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            # may not find exact match
            p = self.find_position(k)
            # p's key is too small
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        """
        Iterate all (key, value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                # we initialize p with logic similar to find_ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        """
        Return value associated with key k (raise KeyError if not found).
        """
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            # hook for balanced tree subclasses
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """
        Assign value v to key k, overwriting existing value if present.
        """
        if self.is_empty():
            # from LinkedBinaryTree
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                # replace existing item's value
                p.element()._value = v
                # hook for balanced tree subclasses
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    # inherited from LinkedBinaryTree
                    leaf = self._add_right(p, item)
                else:
                    # inherited from LinkedBinaryTree
                    leaf = self._add_left(p, item)
        # hook for balanced tree subclasses
        self._rebalance_insert(leaf)

    def __iter__(self):
        """
        Generate an iteration of all keys in the map in order.
        """
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p: Position) -> None:
        """
        Remove the item at given Position.
        """
        # inherited from LinkedBinaryTree
        self._validate(p)
        # p has two children
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            # from LinkedBinaryTree
            self._replace(p, replacement.element())
            p = replacement
        # now p has at most one child
        parent = self.parent(p)
        # inherited from LinkedBinaryTree
        self._delete(p)
        # if root deleted, parent is None
        self._rebalance_delete(parent)

    def __delitem__(self, k):
        """
        Remove item associated with key k (raise KeyError if not found).
        """
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                # rely on positional version
                self.delete(p)
                # successful deletion complete
                return
            # hook for balanced tree subclasses
            self._rebalance_access(p)
        raise KeyError('Key Error: ' + repr(k))

    # template method，交由子类实现，用于平衡树
    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _rebalance_access(self, p):
        pass

    # 平衡树的操作
    def _relink(self, parent, child, make_left_child) -> None:
        """
        Relink parent node with child node (we allow child to be None).
        """
        # make it a left child
        if make_left_child:
            parent._left = child
        # make it a right child
        else:
            parent._right = child
        # make child point to parent
        if child is not None:
            child._parent = parent

    def _rotate(self, p) -> None:
        """
        Rotate Position p above its parent.
        """
        x = p._node
        # we assume this exists
        y = x._parent
        # grandparent (possibly None)
        z = y._parent
        if z is None:
            # x becomes root
            self._root = x
            x._parent = None
        else:
            # x becomes a direct child of z
            self._relink(z, x, y == z._left)
        # now rotate x and y, including transfer of middle subtree
        if x == y._left:
            # x._right becomes left child of y
            self._relink(y, x._right, True)
            # y becomes right child of x
            self._relink(x, y, False)
        else:
            # x._left becomes right child of x
            self._relink(y, x._left, False)
            # y becomes left child of x
            self._relink(x, y, True)

    def _restructure(self, x):
        """
        Perform trinode restructure of Position x with parent/grandparent.
        """
        y = self.parent(x)
        z = self.parent(y)
        # matching alignments
        if (x == self.right(y)) == (y == self.right(z)):
            # single rotation (of y)
            self._rotate(y)
            # y is new subtree root
            return y
        # opposite alignments
        else:
            # double rotation (of x)
            self._rotate(x)
            self._rotate(x)
            # x is new subtree root
            return x

# Sample
# t = TreeMap()
# 添加节点
# t[0] = 0
# 获取节点值
# t[0]
# 删除节点
# t.delete(t.find_position(0))
# 获取指定key的位置
# t.find_position(0)
# 获取子树高度
# t.height(t.find_position(0))
# t.find_min()
# t.find_ge(0)
