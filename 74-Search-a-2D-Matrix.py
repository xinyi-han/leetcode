from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i, flag = self.binarySearch(0, m - 1, [matrix[r][0] for r in range(m)], target)
        if flag:
            return True
        if i == 0:
            return False
        j, flag = self.binarySearch(0, n - 1, matrix[i - 1], target)
        return flag

    def binarySearch(self, lo: int, hi: int, lst: List[int], target: int) -> (int, bool):
        if lo > hi:
            return lo, False
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid, True
        elif lst[mid] > target:
            return self.binarySearch(lo, mid - 1, lst, target)
        else:
            return self.binarySearch(mid + 1, hi, lst, target)
