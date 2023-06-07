from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = set()
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                k = j + 1
                m = len(nums) - 1
                while k < m:
                    sum = nums[i] + nums[j] + nums[k] + nums[m]
                    if sum == target:
                        output.add((nums[i], nums[j], nums[k], nums[m]))
                        k += 1
                    elif sum > target:
                        m -= 1
                    else:
                        k += 1
                n = 0
                while j + n < len(nums) and nums[j] == nums[j + n]:
                    n += 1
                j += n
            p = 0
            while i + p < len(nums) and nums[i] == nums[i + p]:
                p += 1
            i += p
        output = list(map(list, output))
        return output
