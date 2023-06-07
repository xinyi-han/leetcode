class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(Node(val, val))
        else:
            minVal = self.stack[-1].minVal
            minVal = min(minVal, val)
            self.stack.append(Node(val, minVal))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].minVal


class Node:
    def __init__(self, val: int, minVal: int):
        self.val = val
        self.minVal = minVal
