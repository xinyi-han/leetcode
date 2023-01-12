from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum = 0
        maxLen = 0
        hashMap = dict()
        for stick in matchsticks:
            sum += stick
            maxLen = max(maxLen, stick)
            hashMap[stick] = hashMap.get(stick, 0) + 1
        length = sum // 4
        if sum % 4 != 0 or maxLen > length:
            return False
        sticks = list(hashMap.keys())
        sticks.sort(reverse=True)

        def dfs(edgeLen: int, edgeNum: int, i: int) -> bool:
            if edgeNum == 4:
                return True
            for j in range(i, len(sticks)):
                stick = sticks[j]
                if hashMap[stick] == 0:
                    continue
                currLen = edgeLen + stick
                if currLen > length:
                    continue
                hashMap[stick] -= 1
                if currLen < length:
                    if dfs(currLen, edgeNum, j):
                        return True
                else:
                    if dfs(0, edgeNum + 1, 0):
                        return True
                hashMap[stick] += 1
            return False

        return dfs(0, 0, 0)
