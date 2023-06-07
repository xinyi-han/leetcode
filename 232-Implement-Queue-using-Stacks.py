class MyQueue:

    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack2) == 0:
            length = len(self.stack1)
            for i in range(length):
                val = self.stack1.pop()
                self.stack2.append(val)
        return self.stack2.pop()

    def peek(self) -> int:
        if len(self.stack2) > 0:
            return self.stack2[-1]
        return self.stack1[0]

    def empty(self) -> bool:
        return len(self.stack1) + len(self.stack2) == 0
