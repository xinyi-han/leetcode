from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = list()
        if root is None:
            return output
        stack = [root]
        while len(stack) > 0:
            row = list()
            output.append(stack[-1].val)
            for node in stack:
                if node.left is not None:
                    row.append(node.left)
                if node.right is not None:
                    row.append(node.right)
            stack = row
        return output
