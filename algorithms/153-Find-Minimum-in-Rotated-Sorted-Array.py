from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        i = self.binarySearch(0, len(nums) - 1, nums)
        return nums[i]

    def binarySearch(self, lo: int, hi: int, nums: List[int]) -> int:
        if lo > hi:
            return lo
        mid = (lo + hi) // 2
        if nums[mid] < nums[0]:
            return self.binarySearch(lo, mid - 1, nums)
        elif nums[mid] > nums[-1]:
            return self.binarySearch(mid + 1, hi, nums)
