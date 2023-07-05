from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        l = self.tree2str(root.left)
        r = self.tree2str(root.right)
        if len(l) == 0 and len(r) == 0:
            return f"{root.val}"
        elif len(l) == 0:
            return f"{root.val}()({r})"
        elif len(r) == 0:
            return f"{root.val}({l})"
        else:
            return f"{root.val}({l})({r})"
