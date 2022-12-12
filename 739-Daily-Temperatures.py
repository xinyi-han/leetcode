from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for _ in temperatures]
        stack = list()
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < temp:
                j = stack.pop()
                output[j] = i - j
            stack.append(i)
        return output
