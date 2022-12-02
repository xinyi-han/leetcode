from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rev = list(nums)
        rev.reverse()
        return max(self.circleRob(nums), self.circleRob(rev))

    def circleRob(self, nums: List[int]) -> int:
        cache = [0 for _ in range(len(nums) + 1)]
        houses = [set() for _ in range(len(nums) + 1)]
        cache[1] = nums[0]
        houses[1].add(0)
        for i, num in enumerate(nums[1:], 1):
            if i == len(nums) - 1:
                if 0 in houses[i - 1]:
                    cache[i + 1] = max(cache[i], cache[i - 1])
                else:
                    cache[i + 1] = max(cache[i], cache[i - 1] + num)
            else:
                if cache[i] >= cache[i - 1] + num:
                    cache[i + 1] = cache[i]
                    houses[i + 1].update(houses[i])
                else:
                    cache[i + 1] = cache[i - 1] + num
                    houses[i + 1].update(houses[i - 1])
                    houses[i + 1].add(i)
        return cache[-1]
