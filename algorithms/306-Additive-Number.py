class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False

        def backtrack(num1: int, num2: int, i: int) -> bool:
            if i == len(num):
                return True
            sum = num1 + num2
            length = len(str(sum))
            num3 = num[i:i+length]
            if len(num3) > 1 and num3[0] == "0":
                return False
            num3 = int(num3)
            if sum != num3:
                return False
            return backtrack(num2, num3, i + length)

        for i in range(1, len(num) - 1):
            num1 = num[:i]
            if len(num1) > 1 and num1[0] == "0":
                continue
            num1 = int(num1)
            for j in range(i + 1, len(num)):
                num2 = num[i:j]
                if len(num2) > 1 and num2[0] == "0":
                    break
                num2 = int(num2)
                if backtrack(num1, num2, j):
                    return True
        return False
