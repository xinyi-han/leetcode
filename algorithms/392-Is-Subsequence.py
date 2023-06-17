class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i = 0
        while i < len(t):
            if t[i] == s[0]:
                return self.isSubsequence(s[1:], t[i+1:])
            i += 1
        return self.isSubsequence(s, t[i+1:])
