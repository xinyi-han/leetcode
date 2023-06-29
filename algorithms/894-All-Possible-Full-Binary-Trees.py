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
            return list()
        if n == 1:
            return [TreeNode()]
        output = list()
        for i in range(1, n - 1, 2):
            ls = self.allPossibleFBT(i)
            rs = self.allPossibleFBT(n - 1 - i)
            for l in ls:
                for r in rs:
                    node = TreeNode(left=l, right=r)
                    output.append(node)
        return output
