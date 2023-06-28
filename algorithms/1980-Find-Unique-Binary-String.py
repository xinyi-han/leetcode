from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        stack = list()

        def dfs(i: int):
            if i == n:
                num = "".join(stack)
                return None if num in nums else num
            for char in "01":
                stack.append(char)
                num = dfs(i + 1)
                if num is not None:
                    return num
                stack.pop()
            return None

        return dfs(0)
