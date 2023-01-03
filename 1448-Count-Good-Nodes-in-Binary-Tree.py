# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.num = 0

        def topDown(node: TreeNode, maxVal: int):
            if node is None:
                return
            if node.val >= maxVal:
                self.num += 1
            maxVal = max(maxVal, node.val)
            topDown(node.left, maxVal)
            topDown(node.right, maxVal)

        topDown(root, root.val)
        return self.num
