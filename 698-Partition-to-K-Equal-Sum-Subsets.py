from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum = 0
        maxNum = 0
        hashMap = dict()
        for num in nums:
            sum += num
            maxNum = max(maxNum, num)
            hashMap[num] = hashMap.get(num, 0) + 1
        partition = sum // k
        if sum % k != 0 or maxNum > partition:
            return False
        hashSet = list(hashMap.keys())
        hashSet.sort(reverse=True)

        def dfs(subsetSum: int, subsetNum: int, i: int) -> bool:
            if subsetNum == k and subsetSum == 0:
                return True
            for j in range(i, len(hashSet)):
                num = hashSet[j]
                if hashMap[num] == 0:
                    continue
                currSum = subsetSum + num
                if currSum > partition:
                    continue
                hashMap[num] -= 1
                if currSum < partition:
                    if dfs(currSum, subsetNum, j):
                        return True
                else:
                    if dfs(0, subsetNum + 1, 0):
                        return True
                hashMap[num] += 1
            return False

        return dfs(0, 0, 0)
