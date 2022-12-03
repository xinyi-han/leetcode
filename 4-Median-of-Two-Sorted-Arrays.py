from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            small = nums1
            big = nums2
        else:
            small = nums2
            big = nums1
        total = len(nums1) + len(nums2)
        half = total // 2
        lo = 0
        hi = len(small) - 1
        while True:
            midS = (lo + hi) // 2
            midB = half - (midS + 1) - 1

            leftS = small[midS] if midS >= 0 else float('-inf')
            rightS = small[midS + 1] if midS + 1 < len(small) else float('inf')
            leftB = big[midB] if midB >= 0 else float('-inf')
            rightB = big[midB + 1] if midB + 1 < len(big) else float('inf')

            if leftS <= rightB and leftB <= rightS:
                # odd
                if total % 2 == 1:
                    return min(rightS, rightB)
                # even
                else:
                    return (max(leftS, leftB) + min(rightS, rightB)) / 2
            elif leftS > rightB:
                hi = midS - 1
            else:
                lo = midS + 1
