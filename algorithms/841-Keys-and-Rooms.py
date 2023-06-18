from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = {i: False for i in range(len(rooms))}
        visit[0] = True
        keys = set(rooms[0])
        while len(keys) > 0:
            newKeys = set()
            for key in keys:
                visit[key] = True
                for newKey in rooms[key]:
                    if not visit[newKey]:
                        newKeys.add(newKey)
            keys = newKeys
        return sum(visit.values()) == len(rooms)
