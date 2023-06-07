from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        prev = 1
        for num in nums[:-1]:
            prev *= num
            output.append(prev)
        prev = 1
        for i in range(1, len(nums)):
            prev *= nums[-i]
            output[-(i + 1)] *= prev
        return output
