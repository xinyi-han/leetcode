from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        cache = dict()

        def dfs(i: int, sum: int) -> bool:
            if sum == 0:
                return True
            if i == len(nums):
                return False
            if (i, sum) in cache:
                return cache[(i, sum)]
            cache[(i, sum)] = dfs(i + 1, sum - nums[i]) or dfs(i + 1, sum)
            return cache[(i, sum)]

        return dfs(0, total // 2)
