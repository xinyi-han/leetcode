from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = list()
        m = len(matrix)
        n = len(matrix[0])
        round = min(m // 2, n // 2)
        k = 0
        while k < round:
            for i in range(0 + k, n - 1 - k):
                output.append(matrix[0 + k][i])
            for j in range(0 + k, m - 1 - k):
                output.append(matrix[j][n - 1 - k])
            for i in range(1 + k, n - k):
                output.append(matrix[m - 1 - k][-i])
            for j in range(1 + k, m - k):
                output.append(matrix[-j][0 + k])
            k += 1
        if min(m, n) % 2 == 1:
            if m == n:
                output.append(matrix[k][k])
            elif m > n:
                for i in range(k, m - k):
                    output.append(matrix[i][k])
            else:
                for j in range(k, n - k):
                    output.append(matrix[k][j])
        return output
