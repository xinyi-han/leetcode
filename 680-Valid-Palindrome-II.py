from typing import Tuple


class Solution:
    def validPalindrome(self, s: str) -> bool:
        flag, i, j = self.isPalindrome(s)
        if flag:
            return True
        flag, _, _ = self.isPalindrome(s[:i] + s[i+1:])
        if flag:
            return True
        flag, _, _ = self.isPalindrome(s[:j] + s[j+1:])
        return flag


    def isPalindrome(self, s: str) -> Tuple[bool, int, int]:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False, i, j
            i += 1
            j -= 1
        return True, i, j
