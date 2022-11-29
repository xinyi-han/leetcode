# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode()
        node = dummy
        nodes = list()
        left -= 1
        right -= 1
        if left > 0:
            i = 0
            while i < left:
                node.next = head
                node = node.next
                head = head.next
                i += 1
        j = 0
        while j < right - left + 1:
            nodes.append(head)
            head = head.next
            j += 1
        nodes.reverse()
        for n in nodes:
            node.next = n
            node = node.next
        node.next = head
        return dummy.next
