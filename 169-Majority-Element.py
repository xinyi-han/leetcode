from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = dict()
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        for k, v in hashMap.items():
            if v > len(nums) // 2:
                return k
