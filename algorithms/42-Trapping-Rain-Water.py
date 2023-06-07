from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeight = max(height)
        h = height.index(maxHeight)
        left = height[:h + 1]
        right = height[h:]
        right.reverse()
        output = self.easyTrap(left) + self.easyTrap(right)
        return output

    def easyTrap(self, height: List[int]) -> int:
        output = 0
        i = 0
        while i < len(height) - 1:
            if height[i] <= height[i + 1]:
                i += 1
                continue
            else:
                j = 0
                while i + j < len(height) and height[i] >= height[i + j]:
                    j += 1
                output += sum([height[i] - h for h in height[i:i+j]])
                i += j
        return output
