from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.pointer = root
        self.stack = list()
        while self.pointer is not None:
            self.stack.append(self.pointer)
            self.pointer = self.pointer.left

    def next(self) -> int:
        self.pointer = self.stack.pop()
        val = self.pointer.val
        self.pointer = self.pointer.right
        while self.pointer is not None:
            self.stack.append(self.pointer)
            self.pointer = self.pointer.left
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
