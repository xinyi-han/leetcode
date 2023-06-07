class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = dict()
        maxLen = 0
        k = 0
        for i, char in enumerate(s):
            if char not in hashMap:
                hashMap[char] = i
            else:
                if len(hashMap) > maxLen:
                    maxLen = len(hashMap)
                j = hashMap[char]
                for letter in s[k:j]:
                    hashMap.pop(letter)
                hashMap[char] = i
                k = j + 1
        # Edge case: s = " "
        if len(hashMap) > maxLen:
            maxLen = len(hashMap)
        return maxLen
