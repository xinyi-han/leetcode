import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums2, nums1), reverse=True)
        nums2 = [num for num, _ in nums]
        nums1 = [num for _, num in nums]
        heap = nums1[:k]
        total = sum(heap)
        heapq.heapify(heap)
        score = total * nums2[k - 1]
        for i in range(k, len(nums1)):
            num = heapq.heappop(heap)
            total -= num
            heapq.heappush(heap, nums1[i])
            total += nums1[i]
            score = max(score, total * nums2[i])
        return score
