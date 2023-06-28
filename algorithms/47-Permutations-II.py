from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hashMap = dict()
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        output = list()
        stack = list()

        def dfs(i: int):
            if i == len(nums):
                output.append(list(stack))
                return
            for num, c in hashMap.items():
                if c == 0:
                    continue
                stack.append(num)
                hashMap[num] -= 1
                dfs(i + 1)
                stack.pop()
                hashMap[num] += 1

        dfs(0)
        return output
