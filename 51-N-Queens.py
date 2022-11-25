from typing import List, Tuple


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        diagonal_pos = set()
        diagonal_neg = set()
        output = list()

        def dfs(stack: List[Tuple[int, int]]):
            if len(stack) == n:
                board = list()
                for r, c in stack:
                    s = "." * c + "Q" + (n - c - 1) * "."
                    board.append(s)
                output.append(board)
                return
            r = len(stack)
            for c in range(n):
                if c in columns:
                    continue
                elif r - c in diagonal_neg:
                    continue
                elif r + c in diagonal_pos:
                    continue
                else:
                    stack.append((r, c))
                    columns.add(c)
                    diagonal_neg.add(r - c)
                    diagonal_pos.add(r + c)
                    dfs(stack)
                    stack.pop()
                    columns.remove(c)
                    diagonal_neg.remove(r - c)
                    diagonal_pos.remove(r + c)

        for i in range(n):
            columns.add(i)
            diagonal_neg.add(0 - i)
            diagonal_pos.add(0 + i)
            dfs([(0, i)])
            columns.remove(i)
            diagonal_neg.remove(0 - i)
            diagonal_pos.remove(0 + i)
        return output
