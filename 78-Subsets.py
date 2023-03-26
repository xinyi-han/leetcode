from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output, stack = list(),list()

        def dfs(i: int):
            if i == len(nums):
                output.append(list(stack))
                return
            stack.append(nums[i])
            dfs(i + 1)
            stack.pop()
            dfs(i + 1)

        dfs(0)
        return output
