from typing import List, Optional


class SegmentTreeNode:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = 0


class NumArray:

    def __init__(self, nums: List[int]):
        self.root = self.buildTree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        self.updateTree(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeTree(self.root, left, right)

    def buildTree(self, nums: List[int], start: int, end: int) -> Optional[SegmentTreeNode]:
        if start > end:
            return None
        node = SegmentTreeNode(start, end)
        if start == end:
            node.sum = nums[start]
        else:
            mid = (start + end) // 2
            node.left = self.buildTree(nums, start, mid)
            node.right = self.buildTree(nums, mid + 1, end)
            node.sum = node.left.sum + node.right.sum
        return node

    def updateTree(self, root: SegmentTreeNode, index: int, val: int):
        if root.start == root.end:
            root.sum = val
            return
        mid = (root.start + root.end) // 2
        if index <= mid:
            node = root.left
        else:
            node = root.right
        self.updateTree(node, index, val)
        root.sum = root.left.sum + root.right.sum

    def sumRangeTree(self, root: SegmentTreeNode, left: int, right: int) -> int:
        if root.start == left and root.end == right:
            return root.sum
        mid = (root.start + root.end) // 2
        if right <= mid:
            return self.sumRangeTree(root.left, left, right)
        if left > mid:
            return self.sumRangeTree(root.right, left, right)
        l = self.sumRangeTree(root.left, left, mid)
        r = self.sumRangeTree(root.right, mid + 1, right)
        return l + r
