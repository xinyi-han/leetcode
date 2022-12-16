from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k + 1
        heapq.heapify(nums)
        i = 0
        num = None
        while i < k:
            num = heapq.heappop(nums)
            i += 1
        return num
