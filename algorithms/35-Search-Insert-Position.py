from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)

    def binarySearch(self, lo: int, hi: int, nums: List[int], target: int):
        if lo > hi:
            return lo
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearch(lo, mid - 1, nums, target)
        else:
            return self.binarySearch(mid + 1, hi, nums, target)
