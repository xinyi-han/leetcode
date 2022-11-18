from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i, num in enumerate(nums):
            if target - num not in hashMap:
                hashMap[num] = i
            else:
                j = hashMap[target - num]
                return [j, i]
