from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lo = max(nums)
        hi = sum(nums)
        output = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.canSplit(mid, nums, k):
                output = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return output

    def canSplit(self, maxSum: int, nums: List[int], k: int) -> bool:
        subarrayNum = 0
        sum = 0
        for num in nums:
            sum += num
            if sum > maxSum:
                subarrayNum += 1
                sum = num
        return subarrayNum + 1 <= k
