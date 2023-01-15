from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        output = [""]

        def dfs(i: int, stack: List[int], remove: List[int]):
            if i == len(s):
                indices = set(stack + remove)
                result = ""
                for j in range(len(s)):
                    if j in indices:
                        continue
                    result += s[j]
                while len(output) > 0 and len(result) > len(output[-1]):
                    output.pop()
                if len(output) == 0 or len(result) == len(output[-1]):
                    output.append(result)
                return
            if s[i].isalpha():
                dfs(i + 1, stack, remove)
            elif s[i] == "(":
                stack.append(i)
                dfs(i + 1, stack, remove)
                stack.pop()
            else:
                remove.append(i)
                dfs(i + 1, stack, remove)
                remove.pop()
                if len(stack) != 0:
                    # k = stack.pop()
                    # dfs(i + 1, stack, remove)
                    # stack.append(k)
                    # Edge case: s = "(((k()(("
                    for k in range(len(stack)):
                        copy = list(stack)
                        copy.pop(k)
                        dfs(i + 1, copy, remove)

        dfs(0, [], [])
        return list(set(output))
