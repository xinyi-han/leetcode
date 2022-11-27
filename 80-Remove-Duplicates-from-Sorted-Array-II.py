from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while j < len(nums):
            k = 0
            while j + k < len(nums) and nums[j] == nums[j + k]:
                k += 1
            num = nums[j]
            j += k
            if k > 2:
                k = 2
            for n in range(k):
                nums[i + n] = num
            i += k
        return i
