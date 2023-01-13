from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hashMap = dict()
        for task in tasks:
            hashMap[task] = hashMap.get(task, 0) + 1
        rounds = 0
        for k, v in hashMap.items():
            if v == 1:
                return -1
            div = v // 3
            mod = v % 3
            if mod == 0:
                rounds += div
            else:
                rounds += div + 1
        return rounds
