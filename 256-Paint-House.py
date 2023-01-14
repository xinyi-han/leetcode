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
        prev = [0 for _ in range(3)]
        for r, b, g in costs:
            curr = [r, b, g]
            curr[0] += min(prev[1:])
            curr[1] += min(prev[0], prev[2])
            curr[2] += min(prev[:-1])
            prev = curr
        return min(prev)


costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print(Solution().minCost(costs))
