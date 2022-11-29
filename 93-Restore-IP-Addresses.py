from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        output = list()

        def dfs(stack: List[str], substring: str):
            if len(stack) == 4:
                if len(substring) == 0:
                    ip = ".".join(stack)
                    output.append(ip)
                return
            if len(substring) == 0:
                return
            for i in range(1, min(4, len(substring) + 1)):
                subAddress = substring[:i]
                if i == 3 and int(subAddress) > 255:
                    break
                elif i > 1 and substring[0] == "0":
                    break
                stack.append(subAddress)
                dfs(stack, substring[i:])
                stack.pop()

        dfs(list(), s)
        return output
