class Solution:
    def calculate(self, s: str) -> int:
        chars = list(s)
        stack = list()
        i = 0
        while i < len(chars):
            if chars[i] == " ":
                i += 1
            elif chars[i] == "+" or chars[i] == "-":
                stack.append(chars[i])
                i += 1
            elif chars[i].isdigit():
                if len(stack) == 0:
                    stack.append(chars[i])
                else:
                    stack[-1] += chars[i]
                i += 1
            else:
                operation = chars[i]
                i += 1
                k = 0
                while i + k < len(chars) and (chars[i + k].isdigit() or chars[i + k] == " "):
                    k += 1
                num = int(s[i:i + k])
                if operation == "*":
                    stack[-1] = str(int(stack[-1]) * num)
                elif operation == "/":
                    signal = 1 if int(stack[-1]) >= 0 else -1
                    stack[-1] = str(abs(int(stack[-1])) // num * signal)
                i += k
        return sum(list(map(int, stack)))
