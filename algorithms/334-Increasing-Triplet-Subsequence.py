# https://www.youtube.com/watch?v=41gyzVIx-ds
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        fst, snd = float('inf'), float('inf')
        for num in nums:
            if num <= fst:
                fst = num
            elif num <= snd:
                snd = num
            else:
                return True
        return False
