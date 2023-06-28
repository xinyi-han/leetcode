from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = list()
        stack = list()

        def dfs(i: int):
            if len(stack) == 4:
                if i == len(s):
                    output.append(".".join(stack))
                return
            for j in range(i, min(len(s), i + 3)):
                digits = s[i:j + 1]
                if int(digits) > 255:
                    break
                stack.append(digits)
                dfs(j + 1)
                stack.pop()
                if digits == "0":
                    break

        dfs(0)
        return output
