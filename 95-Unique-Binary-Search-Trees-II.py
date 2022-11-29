from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        output = list()
        partition = list()
        for i in range(1, n + 1):
            partition.append((list(range(1, i)), i, list(range(i + 1, n + 1))))
        for left, root, right in partition:
            trees = self.buildTree(root, left, right)
            output.extend(trees)
        return output

    def buildTree(self, root: int, left: List[int], right: List[int]) -> List[TreeNode]:
        trees = list()
        if len(left) == 0 and len(right) == 0:
            trees.append(TreeNode(root))
        elif len(left) == 0:
            rs = self.partition(right)
            for r in rs:
                node = TreeNode(root)
                node.right = r
                trees.append(node)
        elif len(right) == 0:
            ls = self.partition(left)
            for l in ls:
                node = TreeNode(root)
                node.left = l
                trees.append(node)
        else:
            ls = self.partition(left)
            rs = self.partition(right)
            for l in ls:
                for r in rs:
                    node = TreeNode(root)
                    node.left = l
                    node.right = r
                    trees.append(node)
        return trees

    def partition(self, vals: List[int]) -> List[TreeNode]:
        trees = list()
        for i, val in enumerate(vals):
            tree = self.buildTree(val, vals[:i], vals[i+1:])
            trees.extend(tree)
        return trees
