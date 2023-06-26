from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        prev = prices[0]
        for price in prices:
            if price > prev:
                output += price - prev
            prev = price
        return output
