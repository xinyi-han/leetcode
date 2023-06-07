class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = dict()
        for i, char in enumerate(s):
            if char in hashMap:
                if hashMap[char] != t[i]:
                    return False
            else:
                hashMap[char] = t[i]
        keys = list(hashMap.keys())
        values = set(hashMap.values())
        return len(keys) == len(values)
