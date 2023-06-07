from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def binarySearch(lo: int, hi: int) -> int:
            if lo > hi:
                return hi
            mid = (lo + hi) // 2
            remove = set(removable[:mid+1])
            S = [char for i, char in enumerate(s) if i not in remove]
            if self.isSubsequence("".join(S), p):
                return binarySearch(mid + 1, hi)
            else:
                return binarySearch(lo, mid - 1)

        return 1 + binarySearch(0, len(removable) - 1)

    def isSubsequence(self, s: str, p: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if s[i] == p[j]:
                j += 1
            i += 1
        if j == len(p):
            return True
        return False
