class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        matrix = list()
        i = 0
        k = 1
        while i < len(s):
            row = list()
            j = 0
            while i + j < len(s) and j < numRows - 1:
                row.append(s[i + j])
                j += 1
            row.extend([""] * (numRows - len(row)))
            if k % 2 == 0:
                row.reverse()
            matrix.append(row)
            k += 1
            i += j
        output = ""
        for n in range(numRows):
            column = [matrix[m][n] for m in range(len(matrix))]
            output += "".join(column)
        return output
