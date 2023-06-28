from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        diagP = set()
        diagN = set()
        output = list()

        def dfs(i: int):
            if i == n:
                output.append(["".join(r) for r in board])
                return
            for j in range(n):
                if (j not in cols and
                    i - j not in diagN and
                    i + j not in diagP):
                    board[i][j] = 'Q'
                    cols.add(j)
                    diagN.add(i - j)
                    diagP.add(i + j)
                    dfs(i + 1)
                    board[i][j] = '.'
                    cols.remove(j)
                    diagN.remove(i - j)
                    diagP.remove(i + j)

        dfs(0)
        return output
