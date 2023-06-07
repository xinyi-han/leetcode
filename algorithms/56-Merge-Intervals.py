from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = list()
        intervals.sort()
        output.append(list(intervals[0]))
        for start, end in intervals:
            if start <= output[-1][-1]:
                output[-1][-1] = max(output[-1][-1], end)
            else:
                output.append([start, end])
        return output
