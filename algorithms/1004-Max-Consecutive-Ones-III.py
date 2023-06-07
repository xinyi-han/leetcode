from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        if k == 0:
            i = 0
            while i < len(nums):
                j = 0
                while i + j < len(nums) and nums[i + j] == 0:
                    j += 1
                i += j
                p = 0
                while i + p < len(nums) and nums[i + p] == 1:
                    p += 1
                maxLen = max(maxLen, p)
                i += p
            return maxLen
        pos = [0 for _ in range(k)]
        i = 0
        j = 0
        p = 0
        while i < len(nums):
            while j <= k and i + p < len(nums):
                if nums[i + p] == 0:
                    if j < k:
                        pos[j] = i + p
                        j += 1
                    else:
                        break
                p += 1
            maxLen = max(maxLen, p)
            if i + p == len(nums):
                break
            p -= pos[0] - i + 1
            i = pos[0] + 1
            j -= 1
            pos = pos[1:] + [0]
        return maxLen
