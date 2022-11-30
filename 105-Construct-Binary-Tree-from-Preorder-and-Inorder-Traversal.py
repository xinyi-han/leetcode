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
        index = inorder.index(val)
        left = self.buildTree(preorder[1:index+1], inorder[:index])
        right = self.buildTree(preorder[index+1:], inorder[index+1:])
        node = TreeNode(val, left, right)
        return node
