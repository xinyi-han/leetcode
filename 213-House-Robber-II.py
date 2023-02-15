from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            return max(self.rob_(nums[:-1]), self.rob_(nums[1:]))

    def rob_(self, nums: List[int]) -> int:
        cache = [0 for _ in range(len(nums) + 1)]
        cache[1] = nums[0]
        for i, num in enumerate(nums[1:], 2):
            cache[i] = max(cache[i-1], cache[i-2] + num)
        return cache[-1]
