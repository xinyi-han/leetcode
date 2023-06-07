from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalanced_(node: Optional[TreeNode]) -> Tuple[int, bool]:
            if node is None:
                return 0, True
            lh, lf = isBalanced_(node.left)
            rh, rf = isBalanced_(node.right)
            return max(lh, rh) + 1, (lf and rf and abs(lh - rh) <= 1)

        return isBalanced_(root)[1]
