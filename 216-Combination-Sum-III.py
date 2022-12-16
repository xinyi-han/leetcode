from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = list()

        def backtrack(stack: List[int]):
            if len(stack) == k:
                if sum(stack) == n:
                    output.append(list(stack))
                return
            last = stack[-1]
            for j in range(last + 1, 10):
                stack.append(j)
                backtrack(stack)
                stack.pop()

        for i in range(1, 10):
            backtrack([i])
        return output
