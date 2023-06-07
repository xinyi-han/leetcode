from typing import List
import heapq


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums)
        prev, j = float('-inf'), -1
        while len(nums) > 0:
            num, i = heapq.heappop(nums)
            if num == prev and i - j <= k:
                return True
            prev, j = num, i
        return False
