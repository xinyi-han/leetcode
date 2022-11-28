from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        r, flagR = self.binarySearch(0, m - 1, [matrix[i][0] for i in range(m)], target)
        if flagR:
            return True
        elif r == 0:
            return False
        c, flagC = self.binarySearch(0, n - 1, matrix[r - 1], target)
        if flagC:
            return True
        elif c == n:
            return False
        matrix = [matrix[i][c:] for i in range(r)]
        return self.searchMatrix(matrix, target)

    def binarySearch(self, lo: int, hi: int, lst: List[int], target: int) -> (int, bool):
        if lo > hi:
            return lo, False
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid, True
        elif lst[mid] < target:
            return self.binarySearch(mid + 1, hi, lst, target)
        else:
            return self.binarySearch(lo, mid - 1, lst, target)
