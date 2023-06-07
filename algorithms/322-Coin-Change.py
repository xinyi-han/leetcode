from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [amount + 1 for _ in range(amount + 1)]
        cache[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                else:
                    cache[i] = min(cache[i], 1 + cache[i - coin])
        return cache[-1] if cache[-1] != amount + 1 else -1
