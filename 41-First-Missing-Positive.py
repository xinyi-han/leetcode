from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxNum = len(nums)
        nums = set(nums)
        for num in range(1, maxNum + 1):
            if num not in nums:
                return num
        return maxNum + 1
