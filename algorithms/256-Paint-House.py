from typing import List


# Description:
# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of
# painting each house with a certain color is different. You have to paint all the houses such that no two adjacent
# houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0]
# is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so
# on… Find the minimum cost to paint all houses.
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev = costs[-1]
        for r,g,b in costs[-2::-1]:
            curr = list()
            curr.append(r + min(prev[1:]))
            curr.append(g + min(prev[0], prev[-1]))
            curr.append(b + min(prev[:-1]))
            prev = curr
        return min(prev)


costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print(Solution().minCost(costs))
