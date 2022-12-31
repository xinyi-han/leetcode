from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1 for _ in nums]
        for i in range(len(nums) - 2, -1, -1):
            temp = [cache[j] for j in range(i + 1, len(nums)) if nums[j] > nums[i]]
            maxLen = max(temp) if len(temp) > 0 else 0
            cache[i] = max(cache[i], 1 + maxLen)
        return max(cache)
