from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = list()
        for op in operations:
            if op == "+":
                num = stack[-1] + stack[-2]
                stack.append(num)
            elif op == "D":
                num = 2 * stack[-1]
                stack.append(num)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
