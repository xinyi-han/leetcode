class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = (len(a) - len(b)) * "0" + b
        elif len(a) < len(b):
            a = (len(b) - len(a)) * "0" + a
        carry = 0
        output = ""
        for i in range(1, len(a) + 1):
            sum = int(a[-i]) + int(b[-i]) + carry
            if sum <= 1:
                carry = 0
                output = str(sum) + output
            else:
                carry = 1
                if sum == 2:
                    output = "0" + output
                elif sum == 3:
                    output = "1" + output
        if carry != 0:
            output = "1" + output
        return output
