from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        def buildTree(k: int) -> List[Optional[TreeNode]]:
            if k == 1:
                return [TreeNode()]
            nodes = list()
            for i in range(1, k, 2):
                j = k - 1 - i
                ls = buildTree(i)
                rs = buildTree(j)
                for l in ls:
                    for r in rs:
                        node = TreeNode(0, l, r)
                        nodes.append(node)
            return nodes

        return buildTree(n)
