from .tree import Tree


class BinaryTree(Tree):
    """
    Abstract base class representing a binary tree structure.
    """

    # additional abstract methods
    def left(self, p):
        """
        Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """
        Return a Position representing p's right child.
        Return None if p does not have a right child.
        """
        raise NotImplementedError('must be implemented by subclass')

    # concrete methods implemented in this class
    def sibling(self, p):
        """
        Return a Position representing p's sibling (or None if no sibling).
        """
        parent = self.parent(p)
        # p must be the root
        if parent is None:
            # root has no sibling
            return None
        else:
            if p == self.left(parent):
                # possibly None
                return self.right(parent)
            else:
                # possibly None
                return self.left(parent)

    def children(self, p):
        """
        Generate an iteration of Position representing p's children.
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
