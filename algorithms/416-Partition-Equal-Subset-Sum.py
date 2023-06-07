from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        cache = dict()

        def dfs(i: int, sum: int) -> bool:
            if sum == half:
                return True
            if i == len(nums):
                return False
            if (i, sum) in cache:
                return cache[(i, sum)]
            cache[(i, sum)] = dfs(i + 1, sum + nums[i]) or dfs(i + 1, sum)
            return cache[(i, sum)]

        return dfs(0, 0)
