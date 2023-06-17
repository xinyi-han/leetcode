from collections import deque


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while len(self.queue) > 0 and t - self.queue[0] > 3000:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)
