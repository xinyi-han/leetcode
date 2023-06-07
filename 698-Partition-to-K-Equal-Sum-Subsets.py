from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = 0
        maxNum = 0
        hashMap = dict()
        for num in nums:
            total += num
            maxNum = max(maxNum, num)
            hashMap[num] = hashMap.get(num, 0) + 1
        partition = total // k
        if total % k != 0 or maxNum > partition:
            return False
        keys = list(hashMap.keys())
        keys.sort(reverse=True)

        def dfs(subsetSum: int, subsetNum: int, i: int) -> bool:
            if subsetNum == k:
                return True
            for j, num in enumerate(keys[i:]):
                if hashMap[num] == 0:
                    continue
                if subsetSum + num > partition:
                    continue
                hashMap[num] -= 1
                if subsetSum + num < partition:
                    if dfs(subsetSum + num, subsetNum, i + j):
                        return True
                if subsetSum + num == partition:
                    if dfs(0, subsetNum + 1, 0):
                        return True
                hashMap[num] += 1
            return False

        return dfs(0, 0, 0)
