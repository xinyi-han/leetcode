from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        output = 0
        hashMap = dict()
        for num in nums:
            if k - num not in hashMap or hashMap[k - num] == 0:
                hashMap[num] = hashMap.get(num, 0) + 1
            else:
                hashMap[k - num] -= 1
                output += 1
        return output
