from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hashMap = dict()
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        output = list()
        stack = list()

        def dfs():
            if len(stack) == len(nums):
                output.append(list(stack))
                return
            for num in hashMap:
                if hashMap[num] > 0:
                    hashMap[num] -= 1
                    stack.append(num)
                    dfs()
                    hashMap[num] += 1
                    stack.pop()

        dfs()
        return output
