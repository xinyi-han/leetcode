from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = list()
        stack = list()

        def dfs(i: int):
            if len(stack) == k:
                output.append(list(stack))
                return
            if i > n:
                return
            stack.append(i)
            dfs(i + 1)
            stack.pop()
            dfs(i + 1)

        dfs(1)
        return output
