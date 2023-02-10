from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = list()
        stack = list()
        hashMap = dict()
        for num in nums:
            hashMap[num] = 1

        def dfs():
            if len(stack) == len(nums):
                output.append(list(stack))
                return
            for num in hashMap:
                if hashMap[num] == 1:
                    hashMap[num] -= 1
                    stack.append(num)
                    dfs()
                    hashMap[num] += 1
                    stack.pop()

        dfs()
        return output
