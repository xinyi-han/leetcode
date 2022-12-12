from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hashMap = dict()
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        nums = list(set(nums))
        nums.sort()
        cache = [0 for _ in range(len(nums) + 1)]
        cache[1] = hashMap[nums[0]] * nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num - nums[i - 1] == 1:
                cache[i + 1] = max(cache[i], cache[i - 1] + hashMap[num] * num)
            else:
                cache[i + 1] = cache[i] + hashMap[num] * num
        return cache[-1]
