class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashMap = dict()
        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1
        length = 0
        hasOdd = False
        for k, v in hashMap.items():
            if v % 2 == 0:
                length += v
            elif not hasOdd and v % 2 == 1:
                hasOdd = True
                length += v - 1
            else:
                length += v - 1
        if hasOdd:
            length += 1
        return length
