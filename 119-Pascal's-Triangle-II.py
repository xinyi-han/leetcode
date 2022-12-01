from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        prev = [1, 1]
        i = 2
        while i <= rowIndex:
            curr = [1]
            for j in range(len(prev) - 1):
                curr.append(prev[j] + prev[j + 1])
            curr.append(1)
            prev = curr
            i += 1
        return prev
