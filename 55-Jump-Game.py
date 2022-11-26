from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 1
        while i < len(nums):
            j = 1
            while i + j <= len(nums) and nums[-(i + j)] < j:
                j += 1
            if i + j == len(nums) + 1:
                return False
            i += j
        return True

# Time Limit Exceeded
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         bools = [False for _ in nums]
#         bools[0] = True
#         for i, num in enumerate(nums):
#             for j in range(1, num + 1):
#                 if i + j < len(nums):
#                     if bools[i + j]:
#                         continue
#                     else:
#                         bools[i + j] = True
#         return bools[-1]
