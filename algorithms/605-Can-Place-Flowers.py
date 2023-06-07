from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num = 0
        prev = 0
        for i in range(len(flowerbed) - 1):
            curr = flowerbed[i]
            next = flowerbed[i+1]
            if prev == 0 and next == 0 and curr == 0:
                num += 1
                prev = 1
            else:
                prev = curr
        if prev == 0 and flowerbed[-1] == 0:
            num += 1
        return num >= n
