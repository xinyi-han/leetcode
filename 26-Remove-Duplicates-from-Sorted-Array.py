from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while True:
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j == len(nums):
                return i + 1
            i += 1
            nums[i] = nums[j]
