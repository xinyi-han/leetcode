from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def bfs(node: TreeNode) -> (int, bool):
            if node is None:
                return 0, True
            l, left = bfs(node.left)
            r, right = bfs(node.right)
            height = max(l, r) + 1
            if not left or not right:
                return height, False
            elif abs(l - r) > 1:
                return height, False
            return height, True

        return bfs(root)[-1]
