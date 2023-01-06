# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = list()

        def dfs(node: TreeNode):
            if node is None:
                return
            dfs(node.right)
            if len(stack) > 0:
                prev = stack.pop()
                node.val += prev.val
            stack.append(node)
            dfs(node.left)

        dfs(root)
        return root
