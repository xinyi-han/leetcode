from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        pair = [0, root.val] # [maxHeight, value]

        def dfs(node: Optional[TreeNode], height: int):
            if node is None:
                return
            if height > pair[0]:
                pair[0] = height
                pair[1] = node.val
            dfs(node.left, height + 1)
            dfs(node.right, height + 1)

        dfs(root, 0)
        return pair[-1]
