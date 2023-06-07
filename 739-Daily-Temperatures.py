from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for _ in temperatures]
        stack = list()
        for i, temperature in enumerate(temperatures):
            # if len(stack) == 0 or temperature <= temperatures[stack[-1]]:
            #     stack.append(i)
            # else:
            #     while len(stack) > 0 and temperature > temperatures[stack[-1]]:
            #         j = stack.pop()
            #         output[j] = i - j
            #     stack.append(i)
            while len(stack) > 0 and temperature > temperatures[stack[-1]]:
                j = stack.pop()
                output[j] = i - j
            stack.append(i)
        return output
