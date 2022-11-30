from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        val = postorder[-1]
        index = inorder.index(val)
        left = self.buildTree(inorder[:index], postorder[:index])
        right = self.buildTree(inorder[index+1:], postorder[index:-1])
        node = TreeNode(val, left, right)
        return node
