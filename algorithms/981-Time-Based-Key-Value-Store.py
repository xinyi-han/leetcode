from typing import List, Tuple


class TimeMap:

    def __init__(self):
        self.hashMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = list()
        self.hashMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""
        pairs = self.hashMap[key]
        i = self.binarySearch(0, len(pairs) - 1, pairs, timestamp)
        if i == -1:
            return ""
        return self.hashMap[key][i][0]

    def binarySearch(self, lo: int, hi: int, nums: List[Tuple[str, int]], target: int) -> int:
        if lo > hi:
            return hi
        mid = (lo + hi) // 2
        if nums[mid][1] == target:
            return mid
        elif nums[mid][1] < target:
            return self.binarySearch(mid + 1, hi, nums, target)
        else:
            return self.binarySearch(lo, mid - 1, nums, target)
