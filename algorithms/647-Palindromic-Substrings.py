class Solution:
    def countSubstrings(self, s: str) -> int:
        self.output = 0

        def countPalindrome(i: int, j: int) -> None:
            while i >= 0 and j < len(s) and s[i] == s[j]:
                self.output += 1
                i -= 1
                j += 1

        for i in range(len(s)):
            # odd
            l, r = i, i
            countPalindrome(l, r)
            # even
            l, r = i, i + 1
            countPalindrome(l, r)
        return self.output
