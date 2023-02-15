class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        cache[-1][-1] = True
        for j in range(len(s2) - 1, -1, -1):
            if s2[j:] == s3[len(s1)+j:]:
                cache[-1][j] = True
        for i in range(len(s1) - 1, -1, -1):
            if s1[i:] == s3[len(s2)+i:]:
                cache[i][-1] = True
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if cache[i+1][j] and s1[i] == s3[i+j]:
                    cache[i][j] = True
                elif cache[i][j+1] and s2[j] == s3[i+j]:
                    cache[i][j] = True
        return cache[0][0]
