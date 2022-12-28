from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Edge case: amount = 0
        # if amount == 0:
        #     return 0
        cache = [0 for _ in range(amount + 1)]
        cache[0] = 1
        coins.sort()
        for coin in coins:
            for i in range(1, amount + 1):
                if i < coin:
                    continue
                cache[i] += cache[i - coin]
        return cache[-1]
