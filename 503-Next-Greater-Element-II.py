from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        maxNum = max(nums)
        output = list()
        for i, num in enumerate(nums):
            if num == maxNum:
                output.append(-1)
                continue
            for j in range(i + 1, len(nums)):
                if nums[j] > num:
                    output.append(nums[j])
                    break
            else:
                for j in range(i):
                    if nums[j] > num:
                        output.append(nums[j])
                        break
        return output
