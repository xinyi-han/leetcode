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
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit
