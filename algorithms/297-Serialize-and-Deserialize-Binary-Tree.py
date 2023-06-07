# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        output = list()
        queue = [root]
        while len(queue) > 0:
            row = list()
            vals = list()
            for node in queue:
                if node is None:
                    vals.append("#")
                else:
                    vals.append(str(node.val))
                    row.append(node.left)
                    row.append(node.right)
            output.append(",".join(vals))
            queue = row
        return "/".join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "#":
            return None
        data = data.split("/")
        data = list(map(lambda x: x.split(","), data))
        val = int(data[0][0])
        root = TreeNode(val)
        level = [root]
        for i in range(1, len(data)):
            row = list()
            for j, node in enumerate(level):
                if data[i][2 * j] != "#":
                    val = int(data[i][2 * j])
                    left = TreeNode(val)
                    node.left = left
                    row.append(left)
                if data[i][2 * j + 1] != "#":
                    val = int(data[i][2 * j + 1])
                    right = TreeNode(val)
                    node.right = right
                    row.append(right)
            level = row
        return root
