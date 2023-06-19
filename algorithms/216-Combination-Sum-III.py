from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        stack = list()
        output = list()

        def dfs(i: int, sum: int):
            if len(stack) == k:
                if sum == n:
                    output.append(list(stack))
                return
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                stack.append(nums[j])
                dfs(j + 1, sum + nums[j])
                stack.pop()

        dfs(0, 0)
        return output
