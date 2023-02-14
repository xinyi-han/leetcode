from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [False for _ in range(len(s) + 1)]
        cache[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    cache[i] = cache[i+len(word)]
                if cache[i]:
                    break
        return cache[0]
