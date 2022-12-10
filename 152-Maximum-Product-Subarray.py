from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = nums[0]
        minProd = 1
        maxProd = 1
        for num in nums:
            if num == 0:
                output = max(output, num)
                minProd = 1
                maxProd = 1
                continue
            prod = [num * minProd, num * maxProd, num]
            minProd = min(prod)
            maxProd = max(prod)
            output = max(output, maxProd)
        return output
