from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        maxNum = 0
        while i < len(nums):
            j = 0
            while i + j < len(nums) and nums[i + j] == 0:
                j += 1
            i += j
            if i == len(nums):
                return maxNum
            k = 0
            while i + k < len(nums) and nums[i + k] == 1:
                k += 1
            maxNum = max(maxNum, k)
            i += k
        return maxNum
