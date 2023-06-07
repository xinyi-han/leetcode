from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        row = obstacleGrid[0]
        column = [obstacleGrid[i][0] for i in range(m)]
        if 1 not in set(row):
            for j in range(n):
                obstacleGrid[0][j] = 1
        else:
            for j in range(n):
                if obstacleGrid[0][j] == 1:
                    # obstacleGrid[0][j] = 0
                    for k in range(j, n):
                        obstacleGrid[0][k] = 0
                    break
                else:
                    obstacleGrid[0][j] = 1

        if 1 not in set(column):
            for i in range(1, m):
                obstacleGrid[i][0] = 1
        else:
            for i in range(1, m):
                if obstacleGrid[i][0] == 1:
                    # obstacleGrid[i][0] = 0
                    for k in range(i, m):
                        obstacleGrid[k][0] = 0
                    break
                else:
                    obstacleGrid[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i -1][j]
        return obstacleGrid[-1][-1]
