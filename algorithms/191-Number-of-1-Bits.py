class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n > 0:
            num += n % 2
            n = n // 2
        return num
