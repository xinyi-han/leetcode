from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        output = 0
        prev = 0
        for g in gain:
            prev += g
            output = max(output, prev)
        return output
