from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(1, len(digits) + 1):
            digit = digits[-i] + carry
            carry = digit // 10
            digits[-i] = digit % 10
        if carry != 0:
            digits.insert(0, carry)
        return digits
