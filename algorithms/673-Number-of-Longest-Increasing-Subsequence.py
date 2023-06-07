from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        cache = [[1, 1] for _ in nums] # [length, numLen]
        for i in range(len(nums) - 2, -1, -1):
            maxLen = 0
            num = 1
            for j in range(i + 1, len(nums)):
                if nums[j] <= nums[i]:
                    continue
                if cache[j][0] > maxLen:
                    maxLen = cache[j][0]
                    num = cache[j][1]
                elif cache[j][0] == maxLen:
                    num += cache[j][1]
            cache[i] = [1 + maxLen, num]
        maxLen = 0
        num = 0
        for length, numLen in cache:
            if length > maxLen:
                maxLen = length
                num = numLen
            elif length == maxLen:
                num += numLen
        return num
