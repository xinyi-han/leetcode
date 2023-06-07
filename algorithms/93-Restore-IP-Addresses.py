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
            for j in range(i, min(i + 3, len(s))):
                address = s[i:j+1]
                if address[0] == "0":
                    stack.append("0")
                    dfs(i + 1)
                    stack.pop()
                    break
                if int(address) <= 255:
                    stack.append(address)
                    dfs(j + 1)
                    stack.pop()

        dfs(0)
        return output
