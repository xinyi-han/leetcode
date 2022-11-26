from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        i, flag = self.binarySearch(0, len(intervals) - 1, [start for start, end in intervals], newInterval[0])
        if flag:
            intervals[i][-1] = max(intervals[i][-1], newInterval[-1])
        else:
            intervals = intervals[:i] + [newInterval] + intervals[i:]
        output = list()
        output.append(list(intervals[0]))
        for start, end in intervals:
            if start <= output[-1][-1]:
                output[-1][-1] = max(output[-1][-1], end)
            else:
                output.append([start, end])
        return output

    def binarySearch(self, lo: int, hi: int, lst: List[int], target: int) -> (int, bool):
        if lo > hi:
            return lo, False
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid, True
        elif lst[mid] > target:
            return self.binarySearch(lo, mid - 1, lst, target)
        else:
            return self.binarySearch(mid + 1, hi, lst, target)
