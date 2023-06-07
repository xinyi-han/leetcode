import math


class Solution:
    def numDecodings(self, s: str) -> int:
        groups = list()
        group = ""
        for char in s:
            if char == "0":
                if len(group) == 0:
                    return 0
                elif len(group) > 1:
                    groups.append(group[:-1])
                groups.append(group[-1] + char)
                group = ""
            elif char not in "12":
                groups.append(group + char)
                group = ""
            else:
                group += char
        if len(group) > 0:
            groups.append(group)
        ways = list(map(lambda x: self.decode(x), groups))
        return math.prod(ways)

    def decode(self, s: str) -> int:
        if "0" in s:
            return 1
        cache = [0 for _ in range(len(s) + 1)]
        cache[-1] = 1 # cache[len(s)]
        cache[-2] = 1 # cache[len(s) - 1]
        for i in range(len(s) - 2, -1, -1):
            cache[i] += cache[i+1]
            if int(s[i:i+2]) <= 26:
                cache[i] += cache[i+2]
        return cache[0]
