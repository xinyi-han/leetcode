class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) > 1:
            digits = list(map(int, list(num)))
            num = str(sum(digits))
        return int(num)
