from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        output = list()
        queue = list()
        queue.append(root)
        while len(queue) > 0:
            vals = list()
            level = list()
            for node in queue:
                if node is None:
                    vals.append("#")
                else:
                    vals.append(str(node.val))
                    level.append(node.left)
                    level.append(node.right)
            queue = level
            output.append(",".join(vals))
        return "/".join(output)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "#":
            return None
        data = data.split("/")
        data = list(map(lambda x: x.split(","), data))
        root = TreeNode(int(data[0][0]))
        nodes = [root]
        i = 1
        while i < len(data):
            next = list()
            for j, char in enumerate(data[i]):
                if char == "#":
                    node = None
                else:
                    node = TreeNode(int(char))
                    next.append(node)
                if j % 2 == 0:
                    nodes[j // 2].left = node
                else:
                    nodes[j // 2].right = node
            nodes = next
            i += 1
        return root
