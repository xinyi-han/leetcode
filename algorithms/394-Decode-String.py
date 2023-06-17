class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        output = ""
        while i < len(s):
            while i < len(s) and s[i].isalpha():
                output += s[i]
                i += 1
            if i == len(s):
                break
            num = 0
            while i < len(s) and s[i].isnumeric():
                num *= 10
                num += int(s[i])
                i += 1
            stack = [s[i]]
            j = 1
            while i + j < len(s) and len(stack) > 0:
                if s[i + j] == "[":
                    stack.append("[")
                elif s[i + j] == "]":
                    stack.pop()
                j += 1
            output += num * self.decodeString(s[i+1:i+j-1])
            i += j
        return output
