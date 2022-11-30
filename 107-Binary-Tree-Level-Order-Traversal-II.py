from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = list()

        def bfs(prevQueue: List[TreeNode]):
            if len(prevQueue) == 0:
                return
            currQueue = list()
            vals = list()
            for node in prevQueue:
                if node is None:
                    continue
                vals.append(node.val)
                currQueue.append(node.left)
                currQueue.append(node.right)
            bfs(currQueue)
            if len(vals) > 0:
                output.append(vals)

        bfs([root])
        return output
