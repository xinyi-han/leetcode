from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        for k in range(n):
            for i in range(n):
                if isConnected[i][k] == 1:
                    for j in range(n):
                        if isConnected[k][j] == 1:
                            isConnected[i][j] = 1
        cities = set(range(n))
        num = 0
        for i in range(n):
            if i not in cities:
                continue
            for j, c in enumerate(isConnected[i]):
                if c == 1:
                    cities.remove(j)
            num += 1
        return num
