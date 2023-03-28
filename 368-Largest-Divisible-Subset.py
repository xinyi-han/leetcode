from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = [[num] for num in nums]
        for i in range(len(nums) - 2, -1, -1):
            maxLen = 0
            k = i
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    if len(cache[j]) > maxLen:
                        maxLen = len(cache[j])
                        k = j
            if k != i:
                cache[i] += cache[k]
        maxLen = max(list(map(len, cache)))
        for i in range(len(cache)):
            if len(cache[i]) == maxLen:
                return cache[i]
