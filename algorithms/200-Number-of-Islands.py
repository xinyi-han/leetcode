from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        island = 0

        def dfs(i: int, j: int):
            if (not 0 <= i < m or
                not 0 <= j < n or
                ((i, j) in visit)):
                return
            visit.add((i, j))
            if grid[i][j] == "0":
                return
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + di, j + dj)

        for i in range(m):
            for j in range(n):
                if (i, j) in visit or grid[i][j] == "0":
                    continue
                else:
                    island += 1
                    dfs(i, j)
        return island
