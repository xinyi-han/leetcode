from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tail = nums[-k:]
        for i, num in enumerate(nums[:-k]):
            nums[i + k] = num
        for j in range(k):
            nums[j] = tail[j]
