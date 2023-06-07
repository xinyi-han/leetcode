from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1 for _ in nums]
        for i in range(len(nums) - 2, -1, -1):
            maxLen = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    maxLen = max(maxLen, cache[j])
            cache[i] += maxLen
        return max(cache)
