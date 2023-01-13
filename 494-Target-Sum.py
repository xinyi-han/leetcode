from typing import List
from operator import add, sub


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = dict()

        def dfs(i: int, sum: int) -> int:
            if i == len(nums):
                return 1 if sum == target else 0
            if (i, sum) in cache:
                return cache[(i, sum)]
            cache[(i, sum)] = dfs(i + 1, sum + nums[i]) + dfs(i + 1, sum - nums[i])
            return cache[(i, sum)]

        return dfs(0, 0)


# Time Limit Exceeded
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         operators = [add, sub]
#         self.output = 0
#
#         def dfs(i: int, prevSum: int):
#             if i == len(nums):
#                 if prevSum == target:
#                     self.output += 1
#                 return
#             for op in operators:
#                 currSum = op(prevSum, nums[i])
#                 dfs(i + 1, currSum)
#
#         dfs(0, 0)
#         return self.output
