# https://www.youtube.com/watch?v=7cijrfUkQzc
class Solution:
    def numTilings(self, n: int) -> int:
        cache = [0 for _ in range(n)]
        cache[0] = 1 # n = 1
        if n == 1:
            return cache[-1]
        cache[1] = 2 # n = 2
        if n == 2:
            return cache[-1]
        cache[2] = 5 # n = 3
        # cache[n] = cache[n - 1] + cache[n - 2] + 2 * (cache[n - 3] + ... + cache[0])
        # cache[n] = cache[n - 1] + cache[n - 2] + cache[n - 3] + cache[n - 3] + 2 * (cache[n - 4] + ... + cache[0])
        # cache[n] = cache[n - 1] + cache[n - 3] + (cache[n - 2] + cache[n - 3] + 2 * (cache[n - 4] + ... + cache[0]))
        # cache[n] = cache[n - 1] + cache[n - 3] + cache[n - 1]
        # cache[n] = 2 * cache[n - 1] + cache[n - 3]
        for i in range(3, n):
            cache[i] = (2 * cache[i - 1] + cache[i - 3]) % (10**9 + 7)
        return cache[-1]
