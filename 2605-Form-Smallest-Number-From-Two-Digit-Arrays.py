from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums = nums1.intersection(nums2)
        if len(nums) > 0:
            return min(nums)
        num1 = min(nums1)
        num2 = min(nums2)
        return num1 * 10 + num2 if num1 <= num2 else num2 * 10 + num1
