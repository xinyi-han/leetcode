from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        output = [""]
        hashMap = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                   "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        for digit in digits:
            letters = hashMap[digit]
            temp = list()
            for substring in output:
                for letter in letters:
                    temp.append(substring + letter)
            output = temp
        return output
