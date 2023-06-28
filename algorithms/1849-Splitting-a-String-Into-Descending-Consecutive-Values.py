class Solution:
    def splitString(self, s: str) -> bool:
        stack = list()

        def dfs(i: int) -> bool:
            if i == len(s):
                return True if len(stack) > 1 else False
            for j in range(i, len(s)):
                if len(stack) == 0 or stack[-1] - 1 == int(s[i:j + 1]):
                    stack.append(int(s[i:j + 1]))
                    if dfs(j + 1):
                        return True
                    stack.pop()
            return False

        return dfs(0)
