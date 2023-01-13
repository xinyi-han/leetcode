from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        hashMap = dict()
        for f, t in tickets: # f: from, t: to
            if f not in hashMap:
                hashMap[f] = list()
            hashMap[f].append([t, False])
        output = ['JFK']

        def dfs(airportF: str) -> bool:
            if len(output) == len(tickets) + 1:
                return True
            if airportF not in hashMap:
                return False
            for ticket in hashMap[airportF]:
                if ticket[1]:
                    continue
                airportT = ticket[0]
                ticket[1] = True
                output.append(airportT)
                if dfs(airportT):
                    return True
                ticket[1] = False
                output.pop()
            return False

        dfs('JFK')
        return output
