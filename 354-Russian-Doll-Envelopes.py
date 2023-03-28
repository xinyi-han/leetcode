from typing import List


# Time Limit Exceeded
# 知乎2023.03.04后端 - B 笔试
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        cache = [1 for _ in envelopes]
        for i in range(len(envelopes) - 2, -1, -1):
            w, h = envelopes[i]
            for j in range(i + 1, len(envelopes)):
                dw, dh = envelopes[j]
                if w < dw and h < dh:
                    cache[i] = max(cache[i], 1 + cache[j])
        return max(cache)
