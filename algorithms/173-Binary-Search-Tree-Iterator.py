from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        while root is not None:
            self.stack.append(root)
            root = root.left
        self.curr = None

    def next(self) -> int:
        self.curr = self.stack.pop()
        root = self.curr.right
        while root is not None:
            self.stack.append(root)
            root = root.left
        return self.curr.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
