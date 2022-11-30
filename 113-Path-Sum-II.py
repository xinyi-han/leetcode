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

        def dfs(node: TreeNode, stack: List[int], sum: int):
            val = node.val
            stack.append(val)
            if node.left is None and node.right is None:
                if sum + val == targetSum:
                    output.append(list(stack))
                stack.pop()
                return
            elif node.left is None:
                dfs(node.right, stack, sum + val)
            elif node.right is None:
                dfs(node.left, stack, sum + val)
            else:
                dfs(node.left, stack, sum + val)
                dfs(node.right, stack, sum + val)
            stack.pop()

        if root is None:
            return output
        dfs(root, [], 0)
        return output
