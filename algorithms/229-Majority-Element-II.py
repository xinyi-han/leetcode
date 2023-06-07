from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        k = len(nums) // 3
        i = 0
        output = list()
        while i < len(nums):
            j = 0
            while i + j < len(nums) and nums[i + j] == nums[i]:
                j += 1
            if j > k:
                output.append(nums[i])
            i += j
        return output
