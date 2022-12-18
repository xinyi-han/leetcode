from typing import Tuple


class Solution:
    def calculate(self, s: str) -> int:
        chars = list(s)

        def dfs(i: int) -> Tuple[int, int]:
            stack = list()
            while i < len(chars):
                if chars[i] == " ":
                    i += 1
                elif chars[i] == "(":
                    result, j = dfs(i + 1)
                    if len(stack) == 0:
                        stack.append(str(result))
                    elif stack[-1] == "-":
                        stack[-1] = str((-1) * result)
                    else:
                        stack[-1] = str(result)
                    i = j
                elif chars[i] == ")":
                    break
                elif chars[i] == "+" or chars[i] == "-":
                    stack.append(chars[i])
                    i += 1
                else:
                    if len(stack) == 0:
                        stack.append(chars[i])
                    else:
                        stack[-1] += chars[i]
                    i += 1
            result = sum(list(map(int, stack)))
            return result, i + 1

        output, _ = dfs(0)
        return output
