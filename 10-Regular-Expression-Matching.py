# Time Limit Exceeded
# s = "aaaaaaaaaaaaaaaaaaab"
# p = "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*"
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = dict()

        def dfs(i: int, j: int) -> bool:
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if (i, j) in cache:
                return cache[(i, j)]

            if j + 1 < len(p) and p[j + 1] == "*":
                if i < len(s) and (s[i] == p[j] or p[j] == "."):
                    cache[(i, j)] = dfs(i + 1, j) or dfs(i, j + 2)
                else:
                    cache[(i, j)] = dfs(i, j + 2)
            else:
                if i < len(s) and (s[i] == p[j] or p[j] == "."):
                    cache[(i, j)] = dfs(i + 1, j + 1)
                else:
                    cache[(i, j)] = False
            return cache[(i, j)]

        return dfs(0, 0)
