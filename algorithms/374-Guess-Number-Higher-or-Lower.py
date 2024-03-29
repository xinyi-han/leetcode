# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:

        def binarySearch(lo: int, hi: int) -> int:
            mid = lo + (hi - lo) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                return binarySearch(lo, mid - 1)
            else:
                return binarySearch(mid + 1, hi)

        return binarySearch(1, n)
