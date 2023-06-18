from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = list()
        seq2 = list()

        def dfs(node: TreeNode, seq: List):
            if node.left is None and node.right is None:
                seq.append(node.val)
            elif node.left is None:
                dfs(node.right, seq)
            elif node.right is None:
                dfs(node.left, seq)
            else:
                dfs(node.left, seq)
                dfs(node.right, seq)

        dfs(root1, seq1)
        dfs(root2, seq2)
        return seq1 == seq2
