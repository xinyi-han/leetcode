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
        nodes = [root]
        while len(nodes) > 0:
            queue = list()
            vals = list()
            for node in nodes:
                if node is None:
                    vals.append("#")
                else:
                    vals.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
            output.append(",".join(vals))
            nodes = queue
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
        root = TreeNode(int(data[0][0]))
        nodes = [root]
        i = 1
        while i < len(data):
            queue = list()
            for j, node in enumerate(nodes):
                l, r = data[i][2 * j], data[i][2 * j + 1]
                if l != "#":
                    l = TreeNode(int(l))
                    node.left = l
                    queue.append(l)
                if r != "#":
                    r = TreeNode(int(r))
                    node.right = r
                    queue.append(r)
            i += 1
            nodes = queue
        return root
