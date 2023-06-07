from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = [0 for _ in range(amount + 1)]
        cache[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if coin > i:
                    continue
                cache[i] += cache[i - coin]
        return cache[-1]
