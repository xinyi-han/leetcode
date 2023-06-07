from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums = sorted(nums, key=cmp_to_key(self.cmp), reverse=True)
        num = "".join(nums)
        return str(int(num))

    def cmp(self, num1: str, num2: str) -> int:
        if num1 + num2 > num2 + num1:
            return 1
        elif num1 + num2 < num2 + num1:
            return -1
        else:
            return 0
