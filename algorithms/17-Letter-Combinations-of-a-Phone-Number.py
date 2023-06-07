from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        output = list()
        stack = list()

        def dfs(i: int):
            if i == len(digits):
                output.append("".join(stack))
                return
            for char in hashMap[digits[i]]:
                stack.append(char)
                dfs(i + 1)
                stack.pop()

        if len(digits) > 0:
            dfs(0)
        return output
