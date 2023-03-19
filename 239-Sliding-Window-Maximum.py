from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        output = list()
        for i in range(k):
            # if len(queue) == 0 or nums[i] <= nums[queue[-1]]:
            #     queue.append(i)
            # else:
            #     while len(queue) > 0 and nums[i] > nums[queue[-1]]:
            #         queue.pop()
            #     queue.append(i)
            while len(queue) > 0 and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        for i in range(k, len(nums)):
            j = queue[0]
            output.append(nums[j])
            if j < i - k + 1:
                queue.popleft()
            while len(queue) > 0 and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        output.append(nums[queue[0]])
        return output
