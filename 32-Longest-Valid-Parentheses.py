class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxLen = 0
        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) > 0:
                    maxLen = max(maxLen, i - stack[-1])
                else:
                    stack.append(i)
        return maxLen
