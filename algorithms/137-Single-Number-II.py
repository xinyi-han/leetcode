from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = dict()
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
            if hashMap[num] == 3:
                hashMap.pop(num)
        return list(hashMap.keys())[0]
