from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = list()

        def dfs(node: Optional[TreeNode], num: str):
            if node.left is None and node.right is None:
                nums.append(int(num) * 10 + node.val)
                return
            num += str(node.val)
            if node.left is None:
                dfs(node.right, num)
            elif node.right is None:
                dfs(node.left, num)
            else:
                dfs(node.left, num)
                dfs(node.right, num)

        dfs(root, "0")
        return sum(nums)
