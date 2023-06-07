from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo = 1
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
