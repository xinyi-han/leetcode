from typing import List, Tuple


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        flag, i = self.binarySearch(0, len(nums) - 1, nums, 0)
        if not flag:
            if i == 0 or i == len(nums):
                if i == len(nums):
                    nums.reverse()
                return list(map(lambda x: x**2, nums))
            else:
                i, j = i - 1, i
        else:
            i, j = i - 1, i
        output = list()
        while i >= 0 and j < len(nums):
            if abs(nums[i]) <= abs(nums[j]):
                output.append(nums[i]**2)
                i -= 1
            else:
                output.append(nums[j]**2)
                j += 1
        if i >= 0:
            result = list(map(lambda x: x**2, nums[:i+1]))
            result.reverse()
        else:
            result = list(map(lambda x: x**2, nums[j:]))
        output.extend(result)
        return output

    def binarySearch(self, lo: int, hi: int, nums: List[int], target: int) -> Tuple[bool, int]:
        if lo > hi:
            return False, lo
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return True, mid
        elif nums[mid] < target:
            return self.binarySearch(mid + 1, hi, nums, target)
        else:
            return self.binarySearch(lo, mid - 1, nums, target)
