from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = list()
        stack = list()

        def dfs(i: int, sum: int):
            if sum == target:
                output.append(list(stack))
            if i == len(candidates) or sum >= target:
                return
            stack.append(candidates[i])
            dfs(i, sum + candidates[i])
            stack.pop()
            dfs(i + 1, sum)

        dfs(0, 0)
        return output
