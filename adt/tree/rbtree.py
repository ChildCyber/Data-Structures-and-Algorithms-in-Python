from .bst import TreeMap


class RedBlackTreeMap(TreeMap):
    """
    Sorted map implementation using a red-black tree.
    """

    class _Node(TreeMap._Node):
        """
        Node class for red-black tree maintains bit that denotes color.
        """
        # add additional data member to the Node class
        __slots__ = '_red'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            # new node red by default
            self._red = True

    # positional-based utility methods
    # we consider a nonexistent child to be trivially black
    def _set_red(self, p):
        p._node._red = True

    def _set_black(self, p):
        p._node._red = False

    def _set_color(self, p, make_red: bool):
        p._node._red = make_red

    def _is_red(self, p):
        return p is not None and p._node._red

    def _is_red_leaf(self, p):
        return self._is_red(p) and self.is_leaf(p)

    def _get_red_child(self, p):
        """
        Return a red child of p (or None if no such child).
        """
        for child in (self.left(p), self.right(p)):
            if self._is_red(child):
                return child
            return None

    # support for insertions
    def _rebalance_insert(self, p):
        # new node is always red
        self._resolve_red(p)

    def _resolve_red(self, p):
        if self.is_root(p):
            # make root black
            self._set_black(p)
        else:
            parent = self.parent(p)
            # double red problem
            if self._is_red(parent):
                uncle = self.sibling(parent)
                # Case 1: misshapen 4-node
                if not self._is_red(uncle):
                    # do tirnode restructuring
                    middle = self._restructure(p)
                    # and then fix colors
                    self._set_black(middle)
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                # Case 2: overfull 5-node
                else:
                    grand = self.parent(parent)
                    # grandparent becomes red
                    self._set_red(grand)
                    # its children becomes black
                    self._set_black(self.left(grand))
                    self._set_black(self.right(grand))
                    # recur at red grandparent
                    self._resolve_red(grand)

    # support for deletions
    def _rebalance_delete(self, p):
        if len(self) == 1:
            # special case: ensure that root is black
            self._set_black(self.root())
        elif p is not None:
            p = self.num_children(p)
            # deficit exists unless child is a red leaf
            if n == 1:
                c = next(self.children(p))
                if not self._is_red_leaf(c):
                    self._fix_deficit(p, c)
                # removed black node with red child
                elif n == 2:
                    if self._is_red_leaf(self.left(p)):
                        self._set_black(self.left(p))
                    else:
                        self._set_black(self.right(p))

    def _fix_deficit(self, z, y):
        """
        Resolve black deficit at z, where y is the root of z's heavier subtree.
        """
        # y is black; will apply Case 1 or 2
        if not self._is_red(y):
            x = self._get_red_child(y)
            # Case 1: y is black and has red child x; do "transfer"
            if x is not None:
                old_color = self._is_red(z)
                middle = self._restructure(x)
                # middle gets old color of z
                self._set_color(middle, old_color)
                # children become black
                self._set_black(self.left(middle))
                self._set_black(self.right(middle))
            # Case 2: y is black, but no red children; recolor as "fusion"
            else:
                self._set_red(y)
                if self._is_red(z):
                    # this resolves the problem
                    self._set_black(z)
                elif not self.is_root(z):
                    # recur upward
                    self._fix_deficit(self.parent(z), self.sibling(z))
        # Case 3: y is red; rotate misaligned 3-node and repeat
        else:
            self._rotate(y)
            self._set_black(y)
            self._set_red(z)
            if z == self.right(y):
                self._fix_deficit(z, self.left(z))
            else:
                self._fix_deficit(z, self.right(z))
