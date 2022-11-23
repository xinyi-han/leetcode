from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = float('-inf')
        hashMap = dict()
        i = len(nums) - 1
        while i >= 0:
            if nums[i] >= prev:
                hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
                prev = nums[i]
                i -= 1
            else:
                break
        if i >= 0:
            k = min([k for k, v in hashMap.items() if k > nums[i]])
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
            nums[i] = k
            v = hashMap[k]
            if v == 1:
                hashMap.pop(k)
            else:
                hashMap[k] = v - 1
        pairs = [(k, v) for k, v in hashMap.items()]
        pairs.sort()
        i += 1
        for k, v in pairs:
            for j in range(v):
                nums[i + j] = k
            i += v
