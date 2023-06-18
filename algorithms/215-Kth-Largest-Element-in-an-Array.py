import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda num: -1 * num, nums))
        heapq.heapify(nums)
        i = 0
        num = 0
        while i < k:
            num = heapq.heappop(nums)
            i += 1
        return -1 * num
