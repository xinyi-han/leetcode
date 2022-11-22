from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closeSum = float('inf')
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return target
                elif sum > target:
                    k -= 1
                else:
                    j += 1
                if abs(sum - target) < abs(closeSum - target):
                    closeSum = sum
            m = 0
            while i + m < len(nums) and nums[i] == nums[i + m]:
                m += 1
            i += m
        return closeSum
