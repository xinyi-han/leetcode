from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: Optional[TreeNode], val: int) -> int:
            if node is None:
                return 0
            return (val <= node.val) + dfs(node.left, max(val, node.val)) + dfs(node.right, max(val, node.val))

        return dfs(root, root.val)
