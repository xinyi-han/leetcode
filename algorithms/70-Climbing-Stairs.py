# Bottom up
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            cache[i] = cache[i - 2] + cache[i - 1]
        return cache[-1]


# Top down
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = dict()

        def dfs(level: int):
            if level == n:
                return 1
            if level > n:
                return 0
            if level in cache:
                return cache[level]
            cache[level] = dfs(level + 1) + dfs(level + 2)
            return cache[level]

        return dfs(0)
