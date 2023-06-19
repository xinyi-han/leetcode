from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def binarySearch(lo: int, hi: int):
            mid = lo + (hi - lo) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return binarySearch(lo, mid - 1)
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                return binarySearch(mid + 1, hi)
            else:
                return mid

        return binarySearch(0, len(nums) - 1)
