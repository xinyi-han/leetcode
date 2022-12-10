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
        self.traverse(root)
        self.pointer = 0

    def next(self) -> int:
        val = self.stack[self.pointer]
        self.pointer += 1
        return val

    def hasNext(self) -> bool:
        if self.pointer < len(self.stack):
            return True
        return False

    def traverse(self, node: Optional[TreeNode]):
        if node is None:
            return
        self.traverse(node.left)
        self.stack.append(node.val)
        self.traverse(node.right)
