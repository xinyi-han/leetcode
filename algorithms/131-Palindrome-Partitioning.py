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
                if self.isPalindrome(s[i:j+1]):
                    stack.append(s[i:j+1])
                    dfs(j + 1)
                    stack.pop()

        dfs(0)
        return output

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
