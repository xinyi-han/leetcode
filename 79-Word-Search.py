from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visit = set()

        def dfs(i: int, x: int, y: int) -> bool:
            if i == len(word):
                return True
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != word[i] or (x, y) in visit:
                return False
            visit.add((x, y))
            if dfs(i + 1, x - 1, y):
                return True
            if dfs(i + 1, x + 1, y):
                return True
            if dfs(i + 1, x, y - 1):
                return True
            if dfs(i + 1, x, y + 1):
                return True
            visit.remove((x, y))
            return False

        for r in range(m):
            for c in range(n):
                if dfs(0, r, c):
                    return True
        return False
