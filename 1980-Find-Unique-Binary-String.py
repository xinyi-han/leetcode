from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        self.output = None

        def dfs(s: str) -> bool:
            if len(s) == n:
                if s in nums:
                    nums.remove(s)
                    return False
                self.output = s
                return True
            for char in ["0", "1"]:
                if dfs(s + char):
                    return True
            return False

        dfs("")
        return self.output
