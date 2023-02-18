from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        k = 0
        prevL, prevR = 0, 0
        while prevR < len(nums) - 1:
            currL = prevR + 1
            currR = max([i + nums[i] for i in range(prevL, prevR + 1)])
            k += 1
            prevL, prevR = currL, currR
        return k
