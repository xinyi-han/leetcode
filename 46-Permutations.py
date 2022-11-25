from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums = set(nums)
        output = [[num] for num in nums]
        while len(output[0]) != len(nums):
            temp = list()
            for comb in output:
                copy = set(nums)
                for num in comb:
                    copy.remove(num)
                for num in copy:
                    temp.append(comb + [num])
            output = temp
        return output
