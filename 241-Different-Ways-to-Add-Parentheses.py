from typing import List
import operator


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}

        def topDown(s: str) -> List[int]:
            output = list()
            if s.isdigit():
                return [int(s)]
            for i, char in enumerate(s):
                if not char.isdigit():
                    ls = topDown(s[:i])
                    rs = topDown(s[i+1:])
                    op = ops[char]
                    for l in ls:
                        temp = list(map(lambda r: op(l, r), rs))
                        output.extend(temp)
            return output

        return topDown(expression)
