class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0: # Edge case
            return 0
        if num > 0:
            sign = 1
        else:
            sign = -1
        num = abs(num)
        digits = list(str(num))
        if sign == -1:
            digits.sort(reverse=True)
            return int("".join(digits)) * sign
        digits.sort()
        i = 0
        while i < len(digits):
            if digits[i] != "0":
                break
            i += 1
        return int(digits[i] + "".join(digits[:i]) + "".join(digits[i+1:]))
