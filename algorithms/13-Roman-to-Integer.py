class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        output = 0
        prev = float('inf')
        for symbol in s:
            value = hashMap[symbol]
            output += value
            if value > prev:
                output -= 2 * prev
            prev = value
        return output
