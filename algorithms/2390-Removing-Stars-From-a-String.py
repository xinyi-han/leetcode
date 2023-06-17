class Solution:
    def removeStars(self, s: str) -> str:
        stack = list()
        for char in s:
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)
