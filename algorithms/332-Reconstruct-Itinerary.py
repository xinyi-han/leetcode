from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        hashMap = dict()
        for departure, arrival in tickets:
            if departure not in hashMap:
                hashMap[departure] = list()
            hashMap[departure].append([arrival, True])
        stack = ["JFK"]

        def dfs(airport: str) -> bool:
            if len(stack) == len(tickets) + 1:
                return True
            if airport not in hashMap:
                return False
            for destination in hashMap[airport]:
                if not destination[1]:
                    continue
                destination[1] = False
                stack.append(destination[0])
                if dfs(destination[0]):
                    return True
                stack.pop()
                destination[1] = True
            return False

        dfs("JFK")
        return stack
