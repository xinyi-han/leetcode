from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output, stack = list(), list()

        def dfs(i: int):
            if len(stack) == k:
                output.append(list(stack))
                return
            for j in range(i, n + 1):
                stack.append(j)
                dfs(j + 1)
                stack.pop()

        dfs(1)
        return output