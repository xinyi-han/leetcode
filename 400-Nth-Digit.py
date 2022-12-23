class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 1
        num = 9
        while True:
            if n - num * i < 0:
                break
            n -= num * i
            num *= 10
            i += 1
        div = n // i
        mod = n % i
        if mod == 0:
            s = str(num // 9 + div - 1)
            return int(s[-1])
        else:
            s = str(num // 9 + div)
            return int(s[mod - 1])
