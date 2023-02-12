from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev = -1
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = prev
            prev = max(prev, curr)
        return arr
