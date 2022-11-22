class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        output = 0
        if len(s) == 0:
            return output
        sign = 1
        if s[0] == "+":
            sign = 1
            s = s[1:]
        elif s[0] == "-":
            sign = -1
            s = s[1:]
        while len(s) > 0 and s[0].isdigit():
            output = output * 10 + int(s[0])
            s = s[1:]
        output = sign * output
        output = max(-2**31, min(output, 2**31 - 1))
        return output
