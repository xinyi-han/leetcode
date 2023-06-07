from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i = self.binarySearch(0, len(citations) - 1, citations)
        return len(citations) - i

    def binarySearch(self, lo: int, hi: int, nums: List[int]) -> int:
        if lo > hi:
            return lo
        mid = (lo + hi) // 2
        if nums[mid] == len(nums) - mid:
            return mid
        elif nums[mid] > len(nums) - mid:
            return self.binarySearch(lo, mid - 1, nums)
        else:
            return self.binarySearch(mid + 1, hi, nums)
