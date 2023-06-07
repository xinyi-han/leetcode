from typing import List, Tuple, Set


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        lands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    lands.add((i, j))
        islands = 0
        while len(lands) > 0:
            copy = list(lands)
            self.dfs(copy[0], lands)
            islands += 1
        return islands

    def dfs(self, land: Tuple[int, int], lands: Set[Tuple[int, int]]):
        if land not in lands:
            return
        x, y = land
        lands.remove(land)
        self.dfs((x + 1, y), lands)
        self.dfs((x - 1, y), lands)
        self.dfs((x, y + 1), lands)
        self.dfs((x, y - 1), lands)
