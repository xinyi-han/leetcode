from typing import List
import heapq


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums)
        prev, _ = heapq.heappop(nums)
        maxGap = 0
        while len(nums) > 0:
            curr, _ = heapq.heappop(nums)
            maxGap = max(maxGap, curr - prev)
            prev = curr
        return maxGap
