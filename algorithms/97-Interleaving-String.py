class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = dict()

        def dfs(i: int, j: int):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in cache:
                return cache[(i, j)]
            cache[(i, j)] = False
            if i < len(s1) and s1[i] == s3[i + j]:
                cache[(i, j)] = dfs(i + 1, j)
            if not cache[(i, j)] and j < len(s2) and s2[j] == s3[i + j]:
                cache[(i, j)] = dfs(i, j + 1)
            return cache[(i, j)]

        return dfs(0, 0)
