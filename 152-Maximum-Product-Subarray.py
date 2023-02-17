from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = max(nums)
        prevMin, prevMax = 1, 1
        for num in nums:
            if num == 0:
                prevMin, prevMax = 1, 1
                continue
            currMin = min(prevMin * num, prevMax * num, num)
            currMax = max(prevMin * num, prevMax * num, num)
            output = max(output, currMax)
            prevMin, prevMax = currMin, currMax
        return output
