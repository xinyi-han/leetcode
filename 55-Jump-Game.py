from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [False for _ in nums]
        cache[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            for j in range(1, num + 1):
                if cache[i+j]:
                    cache[i] = True
                    break
        return cache[0]
