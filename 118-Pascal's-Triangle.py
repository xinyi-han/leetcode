from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1], [1, 1]]
        if numRows <= 2:
            return output[:numRows]
        i = 2
        while i < numRows:
            row = [1]
            prev = output[-1]
            for j in range(len(prev) - 1):
                row.append(prev[j] + prev[j + 1])
            row.append(1)
            output.append(row)
            i += 1
        return output
