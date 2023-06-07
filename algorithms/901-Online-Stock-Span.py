class StockSpanner:

    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        span = 1
        while len(self.stack) > 0 and price >= self.stack[-1][0]:
            p, s = self.stack.pop()
            span += s
        self.stack.append((price, span))
        return span
