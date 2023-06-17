from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowMap = dict()
        colMap = dict()
        for r in grid:
            r = tuple(r)
            rowMap[r] = rowMap.get(r, 0) + 1
        for i in range(n):
            c = tuple([r[i] for r in grid])
            colMap[c] = colMap.get(c, 0) + 1
        output = 0
        for j in rowMap:
            if j in colMap:
                output += rowMap[j] * colMap[j]
        return output
