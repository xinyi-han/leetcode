from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        edge = total // 4
        if max(matchsticks) > edge:
            return False
        hashMap = dict()
        for stick in matchsticks:
            hashMap[stick] = hashMap.get(stick, 0) + 1
        hashSet = sorted(list(hashMap.keys()), reverse=True)

        def dfs(i: int, edgeSum: int, edgeNum: int) -> bool:
            if edgeNum == 4:
                return True
            for j in range(i, len(hashSet)):
                stick = hashSet[j]
                if hashMap[stick] == 0 or edgeSum + stick > edge:
                    continue
                hashMap[stick] -= 1
                if edgeSum + stick == edge:
                    if dfs(0, 0, edgeNum + 1):
                        return True
                if dfs(j, edgeSum + stick, edgeNum):
                    return True
                hashMap[stick] += 1
            return False

        return dfs(0, 0, 0)
