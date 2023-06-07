from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        output = list()

        def postOrder(node: TreeNode):
            if node is None:
                return
            postOrder(node.left)
            postOrder(node.right)
            output.append(str(node.val))

        postOrder(root)
        return ",".join(output)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return None
        data = list(map(int, data.split(",")))

        def buildTree(vals: List[int]):
            if len(vals) == 0:
                return None
            pivot = len(vals) - 1
            for i, val in enumerate(vals[:-1]):
                if val > vals[-1]:
                    pivot = i
                    break
            val = vals[-1]
            root = TreeNode(val)
            root.left = buildTree(vals[:pivot])
            root.right = buildTree(vals[pivot:-1])
            return root

        return buildTree(data)
