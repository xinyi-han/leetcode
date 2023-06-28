class Solution:
    def totalNQueens(self, n: int) -> int:
        output = 0
        cols = set()
        diagN = set()
        diagP = set()

        def dfs(i: int):
            nonlocal output
            if i == n:
                output += 1
                return
            for j in range(n):
                if (j not in cols and
                    i + j not in diagP and
                    i - j not in diagN):
                    cols.add(j)
                    diagP.add(i + j)
                    diagN.add(i - j)
                    dfs(i + 1)
                    cols.remove(j)
                    diagP.remove(i + j)
                    diagN.remove(i - j)

        dfs(0)
        return output
