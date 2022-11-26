class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            grid[0][j] = 1
        for i in range(m):
            grid[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
        return grid[-1][-1]
