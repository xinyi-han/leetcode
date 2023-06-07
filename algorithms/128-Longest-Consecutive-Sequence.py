from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        digits = set(nums)
        maxLen = 0
        for num in nums:
            if num - 1 not in digits:
                i = 1
                while num + i in digits:
                    digits.remove(num + i)
                    i += 1
                maxLen = max(maxLen, i)
        return maxLen


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        digits = set(nums)
        maxLen = 0
        for num in nums:
            if num - 1 in digits:
                continue
            i = 1
            while num + i in digits:
                i += 1
            maxLen = max(maxLen, i)
        return maxLen
