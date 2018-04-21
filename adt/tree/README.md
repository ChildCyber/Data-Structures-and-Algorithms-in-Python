## Python List 表示二叉树
```python
tree = [["a", "b"], ["c"], ["d", ["e", "f"]]]

# 根节点右孩子
tree[0][1]
tree[2][1][0]
```

## 二叉树
```python
class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

t = Tree(Tree("a", "b"), Tree("c", "d"))
t.right.left
```

## 多路树
```python
class Tree:
    def __init__(self, kids, sibling=None):
        self.kids = self.val = kids
        self.sibling = sibling

t = Tree(Tree("a", Tree("b", Tree("c", Tree("d")))))
t.kids.sibling.sibling.val
```
