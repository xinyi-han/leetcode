from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        output = list()
        for i in range(1, n + 1):
            if i not in nums:
                output.append(i)
        return output
