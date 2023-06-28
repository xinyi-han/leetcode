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
        hashSet = sorted(list(hashMap.keys()), reverse=True)

        def dfs(i: int, pSum: int, pNum: int) -> bool:
            if pNum == k:
                return True
            for j in range(i, len(hashSet)):
                num = hashSet[j]
                if hashMap[num] == 0 or pSum + num > partition:
                    continue
                hashMap[num] -= 1
                if pSum + num == partition:
                    if dfs(0, 0, pNum + 1):
                        return True
                else:
                    if dfs(j, pSum + num, pNum):
                        return True
                hashMap[num] += 1
            return False

        return dfs(0, 0, 0)
