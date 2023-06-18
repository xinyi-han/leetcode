from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        vars = list()
        for var in equations:
            vars.extend(var)
        vars = set(vars)
        vars = {var: i for i, var in enumerate(vars)}
        n = len(vars)
        variables = [[0.0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            variables[i][i] = 1.0
        for [a, b], val in zip(equations, values):
            i, j = vars[a], vars[b]
            variables[i][j] = val
            variables[j][i] = 1 / val
        for k in range(n):
            for i in range(n):
                if variables[i][k] != 0.0:
                    for j in range(n):
                        if variables[k][j] != 0.0:
                            variables[i][j] = variables[i][k] * variables[k][j]
        output = list()
        for c, d in queries:
            if c not in vars or d not in vars:
                output.append(- 1.0)
            else:
                i, j = vars[c], vars[d]
                res = - 1.0 if variables[i][j] == 0.0 else variables[i][j]
                output.append(res)
        return output
