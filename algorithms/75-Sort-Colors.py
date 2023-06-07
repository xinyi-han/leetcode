from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1
        pairs = [(k, v) for k, v in count.items()]
        pairs.sort()
        i = 0
        for k, v in pairs:
            for j in range(v):
                nums[i + j] = k
            i += v
