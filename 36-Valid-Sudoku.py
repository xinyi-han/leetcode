from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = set(map(str, list(range(1, 10))))
        # row
        for row in board:
            copy = set(digits)
            for cell in row:
                if cell.isdigit():
                    if cell not in copy:
                        return False
                    else:
                        copy.remove(cell)

        # column
        for c in range(9):
            column = [board[r][c] for r in range(9)]
            copy = set(digits)
            for cell in column:
                if cell.isdigit():
                    if cell not in copy:
                        return False
                    else:
                        copy.remove(cell)

        # box
        directions = list()
        for r in range(-1, 2):
            for c in range(-1, 2):
                directions.append((r, c))

        mid = [i for i in range(1, 10) if i % 3 == 1]
        centers = list()
        for r in mid:
            for c in mid:
                centers.append((r, c))

        for r, c in centers:
            copy = set(digits)
            for x, y in directions:
                cell = board[r + x][c + y]
                if cell.isdigit():
                    if cell not in copy:
                        return False
                    else:
                        copy.remove(cell)
        return True
