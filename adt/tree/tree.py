from queue.linkedque import LinkedQueue


class Tree:
    """
    Abstract base class representing a tree structure.
    """

    class Position:
        """
        An abstraction representing the location of a single element.
        """

        def element(self):
            """
            Return the element stored at this Position.
            """
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """
            Return True if other Position represents the same location.
            """
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """
            Return True if other does not represent the same location.
            """
            return not (self == other)

    # abstract methods that concrete subclass must support
    def root(self):
        """
        Return Position representing the tree's root (or None if empty).
        """
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """
        Return Position representing p's parent (or None if p is root).
        """
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """
        Return the number of children that Position p has.
        """
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """
        Generate an integration of Position representing p's children.
        """
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """
        Return the total number of elements in the tree.
        """
        raise NotImplementedError('must be implemented by subclass')

    # concrete methods implemented in this class
    def is_root(self, p: Position) -> bool:
        """
        Return True if Position p represents the root of the tree.
        """
        return self.root() == p

    def is_leaf(self, p: Position) -> bool:
        """
        Return True if Position p does not have any children.
        """
        return self.num_children(p) == 0

    def is_empty(self) -> bool:
        """
        Return True if the tree is empty.
        """
        return len(self) == 0

    def depth(self, p: Position) -> int:
        """
        Return the number of levels separating Position p from the root.
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    # works, but O(n^2) worst-case time
    def _height1(self) -> int:
        """
        Return the height of the tree.
        """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    # time is linear in size of subtree
    def _height2(self, p: Position) -> int:
        """
        Return the height of the subtree rooted at Position p.
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None) -> int:
        """
        Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        """
        Generate an iteration of the tree's elements.
        """
        # use same order as positions()
        for p in self.positions():
            # but yield each element
            yield p.element()

    def preorder(self):
        """
        Generate a preorder iteration of position in the tree.
        """
        if not self.is_empty():
            # start recursion
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """
        Generate a preorder iteration of positions in subtree rooted at p.
        """
        # visit p before its subtree
        yield p
        # for each child c
        for c in self.children(p):
            # do preorder of c's subtree
            for other in self._subtree_preorder(c):
                # yielding each to our caller
                yield other

    def postorder(self):
        """
        Generate a postorder iteration of position in the tree.
        """
        if not self.is_empty():
            # start recursion
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """
        Generate a postorder iteration of position in subtree rooted at p.
        """
        # for each child c
        for c in self.children(p):
            # do postorder of c's subtree
            for other in self._subtree_postorder(c):
                # yielding each to our caller
                yield other
            # visit p after its subtrees
            yield c

    def positions(self):
        """
        Generate an iteration of the tree's positions.
        """
        # return entire preorder iteration
        return self.preorder()

    def breadthfirst(self):
        """
        Generate a breadth-first iteration of the positions of the tree.
        """
        if not self.is_empty():
            # known positions not yet yielded
            fringe = LinkedQueue()
            # starting with the root
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                # remove from front of the queue
                p = fringe.dequeue()
                # report this position
                yield p
                for c in self.children(p):
                    # add children to back of queue
                    fringe.enqueue(c)

    def inorder(self):
        """
        Generate an inorder iteration of position in the tree.
        """
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """
        Generate an inorder iteration of position in subtree rooted at p.
        """
        # if left child exists, traverse its subtree
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        # visit p between its subtree
        yield p
        # if right child exists, traverse its subtree
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
