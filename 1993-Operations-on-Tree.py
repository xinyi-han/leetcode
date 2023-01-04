from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [None for _ in self.parent]
        self.children = dict()
        for c, p in enumerate(parent):
            if p not in self.children:
                self.children[p] = list()
            self.children[p].append(c)

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
        curr = num
        while True:
            if self.locked[curr] is not None:
                return False
            curr = self.parent[curr]
            if curr == -1:
                break
        if num not in self.children:
            return False
        locked = list()
        queue = list(self.children[num])
        while len(queue) > 0:
            children = list()
            for child in queue:
                if self.locked[child] is not None:
                    locked.append(child)
                if child in self.children:
                    children.extend(self.children[child])
            queue = children
        if len(locked) == 0:
            return False
        for node in locked:
            self.locked[node] = None
        self.locked[num] = user
        return True
