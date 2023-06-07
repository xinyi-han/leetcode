from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= m * n
        nums = list()
        for row in grid:
            nums.extend(row)
        nums = nums[-k:] + nums[:-k]
        output = list()
        for i in range(m):
            output.append(nums[0 + i * n : n + i * n])
        return output
