from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = list()
        stack = list()
        if len(s) < 4 or len(s) > 12:
            return output

        def dfs(i: int):
            if len(stack) == 4:
                if i == len(s):
                    output.append(".".join(stack))
                return
            for j in range(i, min(len(s), i + 3)):
                section = s[i:j+1]
                if len(section) > 1 and section[0] == "0":
                    break
                if len(section) == 3 and int(section) > 255:
                    break
                stack.append(section)
                dfs(j + 1)
                stack.pop()

        dfs(0)
        return output
