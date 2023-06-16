from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNum = max(candies)
        return list(map(lambda candy: candy + extraCandies >= maxNum, candies))
