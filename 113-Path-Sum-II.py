from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = list()
        stack = list()

        def dfs(node: Optional[TreeNode], sum: int):
            if node is None:
                return
            stack.append(node.val)
            if node.left is None and node.right is None:
                if sum + node.val == targetSum:
                    output.append(list(stack))
                stack.pop()
                return
            dfs(node.left, sum + node.val)
            dfs(node.right, sum + node.val)
            stack.pop()

        dfs(root, 0)
        return output
