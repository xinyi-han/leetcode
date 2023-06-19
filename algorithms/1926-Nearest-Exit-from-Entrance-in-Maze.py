from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        exits = set()
        visit = set()
        for r in {0, m - 1}:
            for c in range(n):
                if maze[r][c] == "." and [r, c] != entrance:
                    exits.add((r, c))
        for c in {0, n - 1}:
            for r in range(m):
                if maze[r][c] == "." and [r, c] != entrance:
                    exits.add((r, c))
        if len(exits) == 0:
            return -1
        queue = {tuple(entrance)}
        step = 0
        while len(queue) > 0:
            cells = set()
            for r, c in queue:
                if (r, c) in exits:
                    return step
                visit.add((r, c))
                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    if (0 <= r + dr < m and
                        0 <= c + dc < n and
                        maze[r + dr][c + dc] == "." and
                        (r + dr, c + dc) not in visit):
                        cells.add((r + dr, c + dc))
            step += 1
            queue = cells
        return -1
