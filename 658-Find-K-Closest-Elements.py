from typing import List
from collections import deque


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]

        def binarySearch(lo: int, hi: int, nums: List[int], target: int) -> int:
            if lo > hi:
                if abs(nums[lo] - target) < abs(nums[hi] - target):
                    return lo
                else:
                    return hi
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(lo, mid - 1, nums, target)
            else:
                return binarySearch(mid + 1, hi, nums, target)

        i = binarySearch(0, len(arr) - 1, arr, x)
        if k == 1:
            return [arr[i]]
        queue = deque(arr[max(0, i-k):i+k+1])
        while len(queue) > k:
            if abs(queue[0] - x) > abs(queue[-1] - x):
                queue.popleft()
            else:
                queue.pop()
        return list(queue)
