from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        output = 0
        stack = list()

        def dfs(i: int):
            nonlocal output
            if i == len(arr):
                s = "".join(stack)
                output = max(output, len(s))
                return
            if self.is_unique("".join(stack) + arr[i]):
                stack.append(arr[i])
                dfs(i + 1)
                stack.pop()
            dfs(i + 1)

        dfs(0)
        return output

    def is_unique(self, s: str) -> bool:
        return len(s) == len(set(s))
