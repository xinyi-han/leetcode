from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        i = 1
        while i < len(asteroids):
            if len(stack) == 0:
                stack.append(asteroids[i])
            elif stack[-1] * asteroids[i] > 0 or (stack[-1] < 0 and asteroids[i] > 0): # [-1, 1] will never meet
                stack.append(asteroids[i])
            else:
                while len(stack) > 0 and stack[-1] > 0 and asteroids[i] < 0:
                    flag = False
                    if stack[-1] == abs(asteroids[i]):
                        stack.pop()
                    elif stack[-1] < abs(asteroids[i]):
                        stack.pop()
                        flag = True
                        continue
                    break
                if flag:
                    stack.append(asteroids[i])
            i += 1
        return stack
