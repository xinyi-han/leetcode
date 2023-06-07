class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = dict()
        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1
        for char in t:
            if char not in hashMap:
                return False
            hashMap[char] -= 1
            if hashMap[char] == 0:
                hashMap.pop(char)
        return True if len(hashMap) == 0 else False
