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
            else:
                l = isSame(node1.left, node2.left)
                r = isSame(node1.right, node2.right)
                return l and r and node1.val == node2.val

        stack = list()
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            if node.val == subRoot.val:
                if isSame(node, subRoot):
                    return True
        return False
