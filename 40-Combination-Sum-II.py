from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = list()
        stack = list()

        def dfs(i: int, sum: int):
            if sum == target:
                output.append(list(stack))
                return
            if sum > target or i == len(candidates):
                return
            num = candidates[i]
            stack.append(num)
            dfs(i + 1, sum + num)
            stack.pop()
            j = 0
            while i + j < len(candidates) and candidates[i+j] == num:
                j += 1
            dfs(i + j, sum)

        dfs(0, 0)
        return output
