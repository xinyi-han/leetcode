from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return 0, 0
            wl, wol = dfs(node.left)
            wr, wor = dfs(node.right)
            w = wol + wor + node.val
            wo = max(wl, wol) + max(wr, wor)
            return w, wo

        w, wo = dfs(root)
        return max(w, wo)
