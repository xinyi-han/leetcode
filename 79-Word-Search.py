from typing import List, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pos = set()

        def dfs(prev: Tuple[int, int], i: int) -> bool:
            if i == len(word):
                return True
            for dx, dy in directions:
                x, y = prev
                x += dx
                y += dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in pos and board[x][y] == word[i]:
                    pos.add((x, y))
                    if dfs((x, y), i + 1):
                        return True
                    pos.remove((x, y))
            return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    pos.add((r, c))
                    if dfs((r, c), 1):
                        return True
                    pos.remove((r, c))
        return False
