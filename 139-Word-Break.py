from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [False for _ in range(len(s) + 1)]
        cache[-1] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                # len(s) - i + len(word) <= len(s)
                if i >= len(word) and s[len(s) - i:len(s) - i + len(word)] == word:
                    cache[len(s) - i] = cache[len(s) - i + len(word)]
                if cache[len(s) - i]:
                    break
        return cache[0]
