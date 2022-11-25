from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [float('inf') for _ in nums]
        jumps[0] = 0
        for i, num in enumerate(nums):
            for j in range(1, num + 1):
                if i + j < len(nums):
                    jumps[i + j] = min(jumps[i + j], jumps[i] + 1)
        return jumps[-1]


# Time Limit Exceeded
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [set() for _ in nums]
        jumps[0].add(0)
        for i, num in enumerate(nums):
            for j in range(1, num + 1):
                step = min(jumps[i])
                if i + j < len(nums):
                    jumps[i + j].add(step + 1)
        return min(jumps[-1])
