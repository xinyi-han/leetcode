from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = min(list(map(len, strs)))
        if minLen == 0:
            return ""
        length = 0
        for i in range(minLen):
            chars = set(map(lambda x: x[i], strs))
            if len(chars) == 1:
                length += 1
            else:
                break
        return strs[0][:length]
