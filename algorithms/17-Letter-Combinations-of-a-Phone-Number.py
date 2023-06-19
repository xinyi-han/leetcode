from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        stack = list()
        output = list()

        def dfs(i: int):
            if i == len(digits):
                output.append("".join(stack))
                return
            for char in hashMap[digits[i]]:
                stack.append(char)
                dfs(i + 1)
                stack.pop()

        if len(digits) == 0:
            return output
        dfs(0)
        return output
