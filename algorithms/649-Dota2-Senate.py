from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if len(set(senate)) == 1:
            return "Radiant" if senate[0] == 'R' else "Dire"
        queue = deque([senate[0]])
        stack = list()
        for i, s in enumerate(senate[1:], 1):
            if len(queue) == 0:
                queue.append(s)
            elif len(queue) > 0:
                if queue[0] != s:
                    s = queue.popleft()
                    stack.append(s)
                else:
                    queue.append(s)
        return self.predictPartyVictory("".join(queue) + "".join(stack))
