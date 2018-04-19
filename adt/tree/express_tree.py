from .lbtree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    """
    An arithmetic expression tree.
    """

    def __init__(self, token, left=None, right=None):
        """
        Create an expression tree.
        """
        super().__init__()
        if not isinstance(token, str):
            raise TypeError('Token must be a string')

        self._add_root(token)
        if left is not None:
            if token not in '+-*x/':
                raise ValueError('token must be valid operator')
            self._attach(self.root(), left, right)

    def __str__(self):
        """
        Return string representation of the expression.
        """
        # sequence of piecewise strings to compose
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        """
        Append piecewise representation of p's subtree to resulting list.
        """
        if self.is_leaf(p):
            # leaf value as string
            result.append(str(p.element()))
        else:
            # opening parenthesis
            result.append('(')
            # left subtree
            self._parenthesize_recur(self.left(p), result)
            # operator
            result.append(p.element())
            # right subtree
            self._parenthesize_recur(self.right(p), result)
            # closing parenthesis
            result.append(')')

    def evaluate(self):
        """
        Return the numeric result of the expression.
        """
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """
        Return the numeric result of subtree rooted at p.
        """
        if self.is_leaf(p):
            # we assume element is numeric
            return float(p.element())
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:
                return left_val * right_val


def build_expression_tree(tokens):
    """
    Return an Expression Tree based upon by a tokenized expression.
    """
    # use Python list as stack
    s = []
    for t in tokens:
        # t is an operator symbol
        if t in '+-x*/':
            # push the operator symbol
            s.append(t)
        # consider t to be a literal
        elif t not in '()':
            # consider t to be a literal
            s.append(ExpressionTree(t))
        # compose a new tree from three constituent parts
        elif t == ')':
            # right subtree as per LIFO
            right = s.pop()
            # right subtree as per LIFO
            op = s.pop()
            # left subtree
            left = s.pop()
            # re-push tree
            s.append(ExpressionTree(op, left, right))
            # we ignore a left parenthesis
    return s.pop()
