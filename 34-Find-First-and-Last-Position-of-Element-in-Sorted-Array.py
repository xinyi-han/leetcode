from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
        if len(nums) == 0:
            return output
        pos = self.binarySearch(0, len(nums) - 1, nums, target)
        if pos == -1:
            return output
        left = pos
        right = pos
        while True:
            l = self.binarySearch(0, left - 1, nums, target)
            if l == -1:
                break
            else:
                left = min(l, left)
        while True:
            r = self.binarySearch(right + 1, len(nums) - 1, nums, target)
            if r == -1:
                break
            else:
                right = max(r, right)
        return [left, right]

    def binarySearch(self, lo: int, hi: int, nums: List[int], target: int) -> int:
        if lo > hi:
            return -1
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearch(lo, mid - 1, nums, target)
        else:
            return self.binarySearch(mid + 1, hi, nums, target)
