from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        hashMap = dict()
        for f, t in tickets:
            if f not in hashMap:
                hashMap[f] = list()
            hashMap[f].append([t, False])
        stack = ["JFK"]

        def dfs(f: str):
            if len(stack) == len(tickets) + 1:
                return stack
            if f not in hashMap:
                return None
            for i, (t, used) in enumerate(hashMap[f]):
                if used:
                    continue
                stack.append(t)
                hashMap[f][i][1] = True
                itinerary = dfs(t)
                if itinerary is not None:
                    return itinerary
                stack.pop()
                hashMap[f][i][1] = False
            return None

        return dfs("JFK")
