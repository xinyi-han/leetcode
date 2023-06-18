from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node: Optional[TreeNode], sumList: List[int]) -> int:
            if node is None:
                return 0
            sumList = list(map(lambda s: s + node.val, sumList)) + [node.val]
            return dfs(node.left, sumList) + dfs(node.right, sumList) + sum(map(lambda s: s == targetSum, sumList))

        return dfs(root, [])
