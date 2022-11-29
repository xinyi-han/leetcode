import math


class Solution:
    def numDecodings(self, s: str) -> int:
        i = 0
        chunks = list()
        while i < len(s):
            j = 0
            while i + j < len(s) and int(s[i + j]) in {1, 2}:
                j += 1
            j += 1
            chunks.append(s[i:i + j])
            i += j
        ways = list(map(self.decode, chunks))
        return math.prod(ways)

    def decode(self, s: str):
        if len(s) == 1:
            if s == "0":
                return 0
            return 1
        cache = [0 for _ in range(len(s) + 1)]
        cache[0] = 1
        cache[1] = 1
        prev = s[0]
        for i in range(2, len(s) + 1):
            if i == len(s) and s[i - 1] == "0":
                cache[i] = cache[i - 2]
            elif int(prev + s[i - 1]) <= 26:
                cache[i] = cache[i - 1] + cache[i - 2]
            else:
                cache[i] = cache[i - 1]
            prev = s[i - 1]
        return cache[-1]
