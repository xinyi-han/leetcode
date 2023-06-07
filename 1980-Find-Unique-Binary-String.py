from typing import List, Optional


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        stack = list()
        length = len(nums[0])
        nums = set(nums)

        def dfs(i: int) -> Optional[str]:
            if i == length:
                s = "".join(stack)
                return s if s not in nums else None
            for char in "01":
                stack.append(char)
                result = dfs(i + 1)
                if result is not None:
                    return result
                stack.pop()
            return None

        return dfs(0)
