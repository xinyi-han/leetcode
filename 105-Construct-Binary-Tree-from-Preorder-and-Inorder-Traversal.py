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
        i = inorder.index(preorder[0])
        l = self.buildTree(preorder[1:i+1], inorder[:i])
        r = self.buildTree(preorder[i+1:], inorder[i+1:])
        node = TreeNode(preorder[0], l, r)
        return node
