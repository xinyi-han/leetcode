from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        hashMap = {num: 1 for num in nums}
        output = list()
        stack = list()

        def dfs():
            if len(stack) == len(nums):
                output.append(list(stack))
                return
            for num in nums:
                if hashMap[num] > 0:
                    hashMap[num] -= 1
                    stack.append(num)
                    dfs()
                    hashMap[num] += 1
                    stack.pop()

        dfs()
        return output
