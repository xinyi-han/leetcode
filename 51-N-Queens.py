from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = list()
        board = [["." for _ in range(n)] for _ in range(n)]
        col = set()
        diagP = set() # r + c
        diagN = set() # r - c

        def dfs(r: int):
            if r == n:
                result = ["".join(row) for row in board]
                output.append(result)
                return
            for c in range(n):
                if c in col or (r + c) in diagP or (r - c) in diagN:
                    continue
                col.add(c)
                diagP.add(r + c)
                diagN.add(r - c)
                board[r][c] = "Q"
                dfs(r + 1)
                col.remove(c)
                diagP.remove(r + c)
                diagN.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return output
