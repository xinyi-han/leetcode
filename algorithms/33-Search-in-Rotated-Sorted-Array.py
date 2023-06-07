from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)

    def binarySearch(self, lo: int, hi: int, nums: List[int], target: int) -> int:
        if lo > hi:
            return -1
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        # left portion
        if nums[mid] >= nums[lo]:
            if nums[mid] < target:
                return self.binarySearch(mid + 1, hi, nums, target)
            else: # nums[mid] > target
                if target >= nums[lo]:
                    return self.binarySearch(lo, mid - 1, nums, target)
                else: # target < nums[lo]
                    return self.binarySearch(mid + 1, hi, nums, target)
        # right portion
        else:
            if nums[mid] > target:
                return self.binarySearch(lo, mid - 1, nums, target)
            else: # nums[mid] < target
                if target <= nums[hi]:
                    return self.binarySearch(mid + 1, hi, nums, target)
                else: # target > nums[hi]
                    return self.binarySearch(lo, mid - 1, nums, target)
