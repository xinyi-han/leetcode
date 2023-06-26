from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            elif price > buy:
                output = max(output, price - buy)
        return output
