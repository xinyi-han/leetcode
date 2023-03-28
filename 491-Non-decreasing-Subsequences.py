from typing import List


# 知乎2023.03.11后端 - 一面
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        output = set()
        stack = list()

        def dfs(i: int):
            if i == len(nums):
                if len(stack) > 1:
                    output.add(tuple(stack))
                return
            # for j in range(i, len(nums)):
            #     if len(stack) == 0 or nums[j] >= stack[-1]:
            #         stack.append(nums[j])
            #         dfs(j + 1)
            #         stack.pop()
            #     dfs(j + 1)
            if len(stack) == 0 or nums[i] >= stack[-1]:
                stack.append(nums[i])
                dfs(i + 1)
                stack.pop()
            dfs(i + 1)

        dfs(0)
        return list(map(list, output))
