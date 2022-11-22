class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = list()
        for bracket in s:
            if bracket not in pairs:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == pairs[bracket]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
