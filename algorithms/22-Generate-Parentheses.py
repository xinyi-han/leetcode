from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        states = [("", 0, 0)]
        i = 0
        while i < 2 * n:
            temp = list()
            for state in states:
                parentheses, openNum, closeNum = state
                if openNum < n:
                    temp.append((parentheses + "(", openNum + 1, closeNum))
                    if openNum > closeNum:
                        temp.append((parentheses + ")", openNum, closeNum + 1))
                elif openNum == n:
                    temp.append((parentheses + ")", openNum, closeNum + 1))
            i += 1
            states = temp
        return [state[0] for state in states]
