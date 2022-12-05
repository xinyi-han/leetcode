from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = list()
        stack = list()

        def dfs(i: int):
            if i == len(s):
                output.append(list(stack))
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    stack.append(s[i:j+1])
                    dfs(j + 1)
                    stack.pop()

        dfs(0)
        return output

    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
