from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev = 0
        for j in range(n):
            grid[0][j] += prev
            prev = grid[0][j]
        prev = 0
        for i in range(m):
            grid[i][0] += prev
            prev = grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
