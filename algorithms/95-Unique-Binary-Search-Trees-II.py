from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def dfs(vals: List[int]) -> List[Optional[TreeNode]]:
            if len(vals) == 0:
                return [None]
            trees = list()
            for i, val in enumerate(vals):
                ls = dfs(vals[:i])
                rs = dfs(vals[i+1:])
                for l in ls:
                    for r in rs:
                        node = TreeNode(val, l, r)
                        trees.append(node)
            return trees

        return dfs(list(range(1, n + 1)))
