class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 1:
            return s
        elif length == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        maxLen = 1
        substring = s[0]
        for i in range(0, length - 1):
            l, r = self.expand(s, i, i)
            if r - l + 1 > maxLen:
                maxLen = r - l + 1
                substring = s[l:r + 1]
            if s[i] == s[i + 1]:
                l, r = self.expand(s, i, i + 1)
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    substring = s[l:r + 1]
        return substring

    def expand(self, s: str, l: int, r: int) -> (int, int):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return l + 1, r - 1
