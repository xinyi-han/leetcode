class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        while i >= 0:
            while j >= i >= 0 and t[j] != s[i]:
                j -= 1
            if j < i:
                return False
            if t[j] == s[i]:
                i -= 1
                j -= 1
        return True
