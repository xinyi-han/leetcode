from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        total = 0
        j = 0
        for i, num in enumerate(nums):
            if total >= target:
                j = i
                break
            total += num
        if j != 0:
            minLen = j
        else:
            minLen = len(nums)
            j = len(nums) - 1
            total -= nums[-1]
        k = 0
        while j < len(nums):
            while k < j and total - nums[k] + nums[j] >= target:
                total -= nums[k]
                k += 1
            total += nums[j]
            minLen = min(minLen, j - k + 1)
            j += 1
        return minLen
