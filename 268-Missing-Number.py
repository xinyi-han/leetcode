from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (0 + n) * (n + 1) // 2 - sum(nums)
