from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hashMap = dict()
        for c in citations:
            hashMap[c] = hashMap.get(c, 0) + 1
        maxCite = max(list(hashMap.keys()))
        sum = 0
        for c in range(maxCite, -1, -1):
            if c in hashMap:
                sum += hashMap[c]
            if sum >= c:
                return c
