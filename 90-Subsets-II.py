from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = [[]]
        stack = list()
        i = 0
        while True:
            for num in nums[i:]:
                stack.append(num)
                output.append(list(stack))
            stack.pop()
            if len(stack) == 0:
                break
            else:
                while len(stack) > 0 and stack[-1] == nums[-1]:
                    stack.pop()
                if len(stack) == 0:
                    break
                num = stack.pop()
            i = nums.index(num)
            j = 0
            while i + j < len(nums) and nums[i] == nums[i + j]:
                j += 1
            i += j
        return output
