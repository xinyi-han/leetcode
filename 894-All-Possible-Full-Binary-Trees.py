from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        def buildTree(num: int) -> List[Optional[TreeNode]]:
            if num == 1:
                return [TreeNode()]
            num -= 1
            trees = list()
            for i in range(1, num, 2):
                ls = buildTree(i)
                rs = buildTree(num - i)
                for l in ls:
                    for r in rs:
                        node = TreeNode(val=0, left=l, right=r)
                        trees.append(node)
            return trees

        return buildTree(n)
