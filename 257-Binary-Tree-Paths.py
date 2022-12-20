from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = list()

        def topDown(node: Optional[TreeNode], s: str):
            if node.left is None and node.right is None:
                output.append(s)
            elif node.left is None:
                topDown(node.right, s + "->" + str(node.right.val))
            elif node.right is None:
                topDown(node.left, s + "->" + str(node.left.val))
            else:
                topDown(node.right, s + "->" + str(node.right.val))
                topDown(node.left, s + "->" + str(node.left.val))

        topDown(root, str(root.val))
        return output
