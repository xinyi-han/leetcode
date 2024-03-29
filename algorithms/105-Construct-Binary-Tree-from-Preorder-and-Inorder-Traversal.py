from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        val = preorder[0]
        i = inorder.index(val)
        l = self.buildTree(preorder[1:i + 1], inorder[:i])
        r = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        node = TreeNode(val, l, r)
        return node
