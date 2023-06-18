from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.length = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node.left is None and node.right is None:
                return 0, 0
            elif node.left is None:
                rl, rr = dfs(node.right)
                self.length = max(self.length, rr)
                return 0, 1 + rl
            elif node.right is None:
                ll, lr = dfs(node.left)
                self.length = max(self.length, ll)
                return 1 + lr, 0
            else:
                ll, lr = dfs(node.left)
                rl, rr = dfs(node.right)
                self.length = max(self.length, ll, rr)
                return 1 + lr, 1 + rl

        return max(*dfs(root), self.length)
