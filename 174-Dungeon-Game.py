from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        health = [[1 for _ in range(n)] for _ in range(m)]
        health[-1][-1] = max(health[-1][-1], health[-1][-1] - dungeon[-1][-1])
        for i in range(2, m + 1):
            health[-i][-1] = max(health[-i][-1], health[-i + 1][-1] - dungeon[-i][-1])
        for j in range(2, n + 1):
            health[-1][-j] = max(health[-1][-j], health[-1][-j + 1] - dungeon[-1][-j])
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                health[-i][-j] = max(health[-i][-j], min(health[-i][-j + 1], health[-i + 1][-j]) - dungeon[-i][-j])
        return health[0][0]
