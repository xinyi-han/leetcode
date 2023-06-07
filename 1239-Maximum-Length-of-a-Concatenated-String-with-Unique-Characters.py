from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        stack = list()
        self.maxLen = 0

        def isUnique() -> bool:
            s = "".join(stack)
            if len(s) == len(set(s)):
                self.maxLen = max(self.maxLen, len(s))
                return True
            return False

        def dfs(i: int):
            if len(stack) > 0 and not isUnique():
                return
            if i == len(arr):
                return
            stack.append(arr[i])
            dfs(i + 1)
            stack.pop()
            dfs(i + 1)

        dfs(0)
        return self.maxLen
