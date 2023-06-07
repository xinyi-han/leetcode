from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)

        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            if node.val == subRoot.val:
                if isSame(node, subRoot):
                    return True
            if dfs(node.left):
                return True
            if dfs(node.right):
                return True
            return False

        return dfs(root)
