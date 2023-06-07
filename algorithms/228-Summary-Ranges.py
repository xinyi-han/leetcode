from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = list()
        if len(nums) == 0:
            return output
        output.append(str(nums[0]))
        i = 1
        while i < len(nums):
            prev = nums[i - 1]
            k = 0
            while i + k < len(nums) and nums[i + k] - prev == 1:
                prev = nums[i + k]
                k += 1
            if k == 0:
                output.append(str(nums[i]))
                i += 1
            else:
                output[-1] += "->" + str(nums[i + k - 1])
                i += k
        return output
