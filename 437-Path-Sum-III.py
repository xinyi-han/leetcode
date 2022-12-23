from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        stack = list()
        stack.append(root)
        closeList = set()
        closeList.add(None)
        path = list()
        num = 0
        while len(stack) > 0:
            while len(path) > 0 and (path[-1].left in closeList and path[-1].right in closeList):
                vals = list(map(lambda x: x.val, path))
                prev = 0
                for val in vals[::-1]:
                    prev += val
                    if prev == targetSum:
                        num += 1
                path.pop()
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            closeList.add(node)
            path.append(node)
        while len(path) > 0 and (path[-1].left in closeList and path[-1].right in closeList):
            vals = list(map(lambda x: x.val, path))
            prev = 0
            for val in vals[::-1]:
                prev += val
                if prev == targetSum:
                    num += 1
            path.pop()
        return num
