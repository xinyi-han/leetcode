from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        maxArea = 0
        i = 0
        length = len(heights)
        while i < length:
            h = heights[i]
            if len(stack) == 0:
                stack.append((i, h))
            else:
                if stack[-1][-1] <= h:
                    stack.append((i, h))
                else:
                    while len(stack) > 0 and stack[-1][-1] > h:
                        maxArea = max(maxArea, (i - stack[-1][0]) * stack[-1][-1])
                        j, _ = stack.pop()
                    stack.append((j, h))
            i += 1
        if len(stack) > 0:
            for j, h in stack:
                maxArea = max(maxArea, (length - j) * h)
        return maxArea
