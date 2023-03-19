from typing import List


# Time Limit Exceeded
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         cache = [0 for _ in prices]
#         for i in range(len(prices) - 2, -1, -1):
#             for j in range(i, len(prices)):
#                 cache[i] = max(cache[i], prices[j] - prices[i])
#         return max(cache)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxPrice = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            maxProfit = max(maxProfit, maxPrice - prices[i])
            maxPrice = max(maxPrice, prices[i])
        return maxProfit
