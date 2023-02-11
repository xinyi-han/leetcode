from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = list()
        stack = list()

        def dfs(i: int, sum: int):
            if i == len(candidates):
                return
            if sum == target:
                output.append(list(stack))
            if sum >= target:
                return
            num = candidates[i]
            stack.append(num)
            dfs(i, sum + num)
            stack.pop()
            dfs(i + 1, sum)

        dfs(0, 0)
        return output
