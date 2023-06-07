from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        w = j
        maxVolume = 0
        while i < j:
            h = min(height[i], height[j])
            maxVolume = max(maxVolume, h * w)
            w -= 1
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxVolume
