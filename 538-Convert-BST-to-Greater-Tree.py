from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node: Optional[TreeNode], sum: int) -> int:
            if node.left is None and node.right is None:
                node.val += sum
                return node.val
            elif node.left is None:
                val = dfs(node.right, sum)
                node.val += val
                return node.val
            elif node.right is None:
                node.val += sum
                return dfs(node.left, node.val)
            else:
                val = dfs(node.right, sum)
                node.val += val
                return dfs(node.left, node.val)

        if root is None:
            return None
        dfs(root, 0)
        return root
