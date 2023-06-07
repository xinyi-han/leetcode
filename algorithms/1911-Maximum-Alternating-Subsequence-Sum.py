from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        cache = dict()

        def dfs(i: int, isEven: bool) -> int:
            if i == len(nums):
                return 0
            if (i, isEven) in cache:
                return cache[(i, isEven)]
            num = nums[i] if isEven else -1 * nums[i]
            cache[(i, isEven)] = max(num + dfs(i + 1, not isEven), dfs(i + 1, isEven))
            return cache[(i, isEven)]

        return dfs(0, True)
