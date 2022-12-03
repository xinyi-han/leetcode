from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def dfs(pathSum: str, node: TreeNode):
            pathSum += str(node.val)
            if node.left is None and node.right is None:
                self.sum += int(pathSum)
                return
            elif node.left is None:
                dfs(pathSum, node.right)
            elif node.right is None:
                dfs(pathSum, node.left)
            else:
                dfs(pathSum, node.left)
                dfs(pathSum, node.right)

        dfs("", root)
        return self.sum
