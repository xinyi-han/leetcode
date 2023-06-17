from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)
        for i, num in enumerate(nums):
            r -= num
            if l == r:
                return i
            l += num
        return -1
