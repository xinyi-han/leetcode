from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        # 2 -> under-population
        # 3 -> over-population
        # 4 -> reproduction
        for i in range(m):
            for j in range(n):
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if (di, dj) == (0, 0) or not 0 <= i + di < m or not 0 <= j + dj < n:
                            continue
                        if board[i + di][j + dj] in {1, 2, 3}:
                            count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 4
                elif board[i][j] == 1:
                    if count < 2:
                        board[i][j] = 2
                    elif count > 3:
                        board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] in {2, 3}:
                    board[i][j] = 0
                elif board[i][j] == 4:
                    board[i][j] = 1
