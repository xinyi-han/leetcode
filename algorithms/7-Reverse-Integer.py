class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            sign = 1
        else:
            sign = -1
        copy = abs(x)
        output = 0
        while copy > 0:
            remainder = copy % 10
            output = output * 10 + remainder
            copy = copy // 10
            if output > (2**31 - 1) // 10 and copy > 0:
                return 0
            elif output == (2**31 - 1) // 10:
                if copy > 8:
                    return 0
                elif sign == 1:
                    if copy == 8:
                        return 0
        return output * sign
