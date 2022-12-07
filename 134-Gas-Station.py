from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = list(map(lambda x, y: x - y, gas, cost))
        if sum(diff) < 0:
            return -1
        accumulate = 0
        start = 0
        for i in range(len(gas)):
            accumulate += diff[i]
            if accumulate < 0:
                accumulate = 0
                start = i + 1
        return start
