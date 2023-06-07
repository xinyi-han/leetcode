from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = 0
        maxStick = 0
        hashMap = dict()
        for stick in matchsticks:
            total += stick
            maxStick = max(maxStick, stick)
            hashMap[stick] = hashMap.get(stick, 0) + 1
        length = total // 4
        if total % 4 != 0 or maxStick > length:
            return False
        sticks = list(hashMap.keys())
        sticks.sort(reverse=True)

        def dfs(edgeSum: int, edgeNum: int, i: int) -> bool:
            if edgeNum == 4:
                return True
            for j, stick in enumerate(sticks[i:]):
                if hashMap[stick] == 0:
                    continue
                if edgeSum + stick > length:
                    continue
                hashMap[stick] -= 1
                if edgeSum + stick < length:
                    if dfs(edgeSum + stick, edgeNum, i + j):
                        return True
                elif edgeSum + stick == length:
                    if dfs(0, edgeNum + 1, 0):
                        return True
                hashMap[stick] += 1
            return False

        return dfs(0, 0, 0)
