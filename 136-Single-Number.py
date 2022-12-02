from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            if num not in hashSet:
                hashSet.add(num)
            else:
                hashSet.remove(num)
        return list(hashSet)[0]
