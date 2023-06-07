from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ops = {"+", "-", "*"}
        output = list()

        def backtrack(stack: List[str], s: str):
            if s == "":
                if self.calculate(stack, target):
                    output.append("".join(stack))
                return
            for i in range(1, len(s) + 1):
                if i > 1 and s[0] == "0":
                    break
                stack.append(s[:i])
                if i == len(s):
                    backtrack(stack, "")
                else:
                    for op in ops:
                        stack.append(op)
                        backtrack(stack, s[i:])
                        stack.pop()
                stack.pop()

        backtrack([], num)
        return output

    def calculate(self, exps: List[str], target: int) -> bool:
        operands = list()
        i = 0
        op = 1
        while i < len(exps):
            if exps[i].isdigit():
                operands.append(op * int(exps[i]))
            elif exps[i] == "+":
                op = 1
            elif exps[i] == "-":
                op = -1
            elif exps[i] == "*":
                i += 1
                operands[-1] *= int(exps[i])
            i += 1
        return sum(operands) == target
