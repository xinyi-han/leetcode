from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = set()
        rotten = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    rotten.add((r, c))
        if len(fresh) == 0:
            return 0
        minutes = 0
        while len(rotten) > 0:
            rot = set()
            for r, c in rotten:
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if (0 <= r + dr < m and
                        0 <= c + dc < n and
                        (r + dr, c + dc) in fresh):
                        rot.add((r + dr, c + dc))
                        fresh.remove((r + dr, c + dc))
            minutes += 1
            rotten = rot
        return -1 if len(fresh) > 0 else minutes - 1
