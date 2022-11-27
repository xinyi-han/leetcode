from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
            num = stack.pop()
            i = nums.index(num) + 1
        return output
