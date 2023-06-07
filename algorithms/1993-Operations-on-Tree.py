from typing import List
from collections import deque


class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [None for _ in parent]
        self.children = dict()
        for i, child in enumerate(parent):
            if child not in self.children:
                self.children[child] = list()
            self.children[child].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] is not None:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = None
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        ancestor = num
        while ancestor != -1:
            if self.locked[ancestor] is not None:
                return False
            ancestor = self.parent[ancestor]
        descendant = num
        queue = deque()
        queue.append(descendant)
        count = 0
        while len(queue) > 0:
            node = queue.popleft()
            for child in self.children.get(node, []):
                if self.locked[child] is not None:
                    count += 1
                    self.locked[child] = None
                queue.append(child)
        if count == 0:
            return False
        self.locked[num] = user
        return True
