class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        hashMap = dict()
        for i, p in enumerate(pattern):
            word = words[i]
            if p not in hashMap:
                hashMap[p] = word
            elif hashMap[p] != word:
                return False
        return len(list(hashMap.values())) == len(set(hashMap.values()))


# Edge case: pattern = "abc", s = "b c a"
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         words = s.split()
#         if len(pattern) != len(words):
#             return False
#         hashMap = dict()
#         for i, p in enumerate(pattern):
#             word = words[i]
#             if p not in hashMap and word not in hashMap:
#                 hashMap[p] = word
#                 hashMap[word] = p
#             elif p not in hashMap or word not in hashMap:
#                 return False
#             elif hashMap[p] != word:
#                 return False
#         return True
