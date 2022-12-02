from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))

    def dfs(self, root: Optional[TreeNode]) -> List[int]:
        # [with root, without root]
        if root is None:
            return [0, 0]
        else:
            wl, wol = self.dfs(root.left)
            wr, wor = self.dfs(root.right)
            w = root.val + wol + wor
            wo = max(wl, wol) + max(wr, wor)
            return [w, wo]
