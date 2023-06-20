from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0 for _ in range(len(nums) + 1)]
        cache[1] = nums[0]
        for i in range(2, len(cache)):
            cache[i] = max(nums[i - 1] + cache[i - 2], cache[i - 1])
        return cache[-1]
