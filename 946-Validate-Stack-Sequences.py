from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        stack = list()
        while i < len(pushed):
            stack.append(pushed[i])
            while len(stack) > 0 and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            if j == len(popped):
                return True
            i += 1
        return False
