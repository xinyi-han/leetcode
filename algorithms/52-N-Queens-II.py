class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        diagP = set()
        diagN = set()
        self.output = 0

        def dfs(r: int):
            if r == n:
                self.output += 1
                return
            for c in range(n):
                if c in col or (r + c) in diagP or (r - c) in diagN:
                    continue
                col.add(c)
                diagP.add(r + c)
                diagN.add(r - c)
                dfs(r + 1)
                col.remove(c)
                diagP.remove(r + c)
                diagN.remove(r - c)

        dfs(0)
        return self.output
