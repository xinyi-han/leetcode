class Solution:
    def reverseBits(self, n: int) -> int:
        bits = list()
        while n > 0:
            bits.append(n % 2)
            n = n // 2
        if len(bits) < 32:
            bits = bits + [0] * (32 - len(bits))
        output = 0
        i = 0
        while i < len(bits):
            output = output * 2 + bits[i]
            i += 1
        return output
