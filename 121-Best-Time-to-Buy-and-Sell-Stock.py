from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxPrice = prices[-1]
        for i in range(2, len(prices) + 1):
            maxProfit = max(maxProfit, maxPrice - prices[-i])
            maxPrice = max(maxPrice, prices[-i])
        return maxProfit
