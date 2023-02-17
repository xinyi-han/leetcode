from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            nums[i] = max(nums[i], nums[i] + nums[i+1])
            output = max(output, nums[i])
        return output
