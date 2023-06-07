from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = sum(nums[1:])
        for i in range(len(nums) - 1):
            if left == right:
                return i
            left += nums[i]
            right -= nums[i+1]
        if left == right:
            return len(nums) - 1
        else:
            return -1
