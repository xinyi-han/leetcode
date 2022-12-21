from typing import List
import heapq
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        queue.append((nums[0], 0)) # (num, index)
        output = list()
        for i in range(1, k):
            while len(queue) > 0 and nums[i] >= queue[-1][0]:
                queue.pop()
            queue.append((nums[i], i))
        i = k
        while i < len(nums):
            output.append(queue[0][0])
            if i - queue[0][1] == k:
                queue.popleft()
            while len(queue) > 0 and nums[i] >= queue[-1][0]:
                queue.pop()
            queue.append((nums[i], i))
            i += 1
        output.append(queue[0][0])
        return output


# Time Limit Exceeded
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         queue = list()
#         output = list()
#         for i in range(k):
#             queue.append((- nums[i], i, nums[i]))
#         heapq.heapify(queue)
#         i = k
#         while i < len(nums):
#             _, _, num = queue[0]
#             output.append(num)
#             for j, (_, index, _) in enumerate(queue):
#                 if index == i - k:
#                     del queue[j]
#                     break
#             queue.append((- nums[i], i, nums[i]))
#             heapq.heapify(queue)
#             i += 1
#         _, _, num = queue[0]
#         output.append(num)
#         return output
