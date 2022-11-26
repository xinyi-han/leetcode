from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = nums[0]
        for num in nums[1:]:
            if sum + num > num:
                sum += num
            else:
                sum = num
            maxSum = max(maxSum, sum)
        return maxSum
