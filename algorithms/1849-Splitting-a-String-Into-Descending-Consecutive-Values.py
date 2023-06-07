class Solution:
    def splitString(self, s: str) -> bool:
        stack = list()

        def dfs(i: int) -> bool:
            if i == len(s):
                return True if len(stack) > 1 else False # split s into two or more non-empty substrings
            for j in range(i, len(s)):
                num = int(s[i:j+1])
                if len(stack) == 0 or num == stack[-1] - 1:
                    stack.append(num)
                    if dfs(j + 1):
                        return True
                    stack.pop()
            return False

        return dfs(0)
