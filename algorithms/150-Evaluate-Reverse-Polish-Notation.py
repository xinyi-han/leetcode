from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif len(token) == 1:
                y = stack.pop()
                x = stack.pop()
                if token == "+":
                    result = x + y
                elif token == "-":
                    result = x - y
                elif token == "*":
                    result = x * y
                else:
                    result = int(x/y)
                stack.append(result)
            else:
                token = int(token)
                stack.append(token)
        return stack[-1]
