from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nodes = list()
        while head is not None:
            node = TreeNode(head.val)
            nodes.append(node)
            head = head.next
        return self.buildTree(nodes)

    def buildTree(self, nodes: List[TreeNode]) -> Optional[TreeNode]:
        if len(nodes) == 0:
            return None
        mid = (0 + len(nodes) - 1) // 2
        nodes[mid].left = self.buildTree(nodes[:mid])
        nodes[mid].right = self.buildTree(nodes[mid+1:])
        return nodes[mid]
