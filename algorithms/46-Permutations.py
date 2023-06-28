from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = {num: 1 for num in nums}
        output = list()
        stack = list()

        def dfs(i: int):
            if i == len(nums):
                output.append(list(stack))
                return
            for num, c in nums.items():
                if c == 0:
                    continue
                stack.append(num)
                nums[num] -= 1
                dfs(i + 1)
                stack.pop()
                nums[num] += 1

        dfs(0)
        return output
