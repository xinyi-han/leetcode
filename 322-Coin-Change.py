from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        cache = [amount + 1 for _ in range(amount + 1)]
        cache[0] = 0
        coins.sort()
        for i in range(1, amount + 1):
            for j in coins:
                if i < j:
                    # Edge case: coins = [1,2147483647], amount = 2
                    if cache[i] == amount + 1:
                        cache[i] = 0
                    break
                elif i == j:
                    cache[i] = 1
                    break
                else:
                    if cache[i - j] == 0:
                        continue
                    else:
                        cache[i] = min(cache[i], 1 + cache[i - j])
            else:
                if cache[i] == amount + 1:
                    cache[i] = 0
        return cache[-1] if cache[-1] != 0 else -1
