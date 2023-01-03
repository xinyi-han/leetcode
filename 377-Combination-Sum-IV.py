from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = [0 for _ in range(target + 1)]
        cache[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    continue
                cache[i] += cache[i - num]
        return cache[-1]
