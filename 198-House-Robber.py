from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0 for _ in range(len(nums) + 1)]
        cache[1] = nums[0]
        for i, num in enumerate(nums[1:], 1):
            cache[i + 1] = max(cache[i - 1] + num, cache[i])
        return cache[-1]
