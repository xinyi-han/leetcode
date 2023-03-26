from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output, stack = list(), list()

        def dfs(i: int):
            if i == len(nums):
                output.append(list(stack))
                return
            stack.append(nums[i])
            dfs(i + 1)
            stack.pop()
            j = 0
            while i + j < len(nums) and nums[i] == nums[i + j]:
                j += 1
            dfs(i + j)

        dfs(0)
        return output
