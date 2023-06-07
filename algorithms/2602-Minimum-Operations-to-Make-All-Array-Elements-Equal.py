from typing import List, Tuple


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        length = len(nums)
        leftSum, rightSum = [0 for _ in nums], [0 for _ in nums]
        l, r = 0, 0
        for i, num in enumerate(nums):
            leftSum[i] = l
            l += num
        total = l
        for j, num in enumerate(nums[::-1], 1):
            rightSum[-j] = r
            r += num
        output = list()
        for query in queries:
            k, flag = self.binarySearch(0, length - 1, nums, query)
            if flag:
                output.append((k * query - leftSum[k]) + (rightSum[k] - (length - 1 - k) * query))
                continue
            if k == 0:
                output.append(total - length * query)
            elif k == length:
                output.append(length * query - total)
            else:
                output.append((k * query - leftSum[k]) + (rightSum[k] - (length - 1 - k) * query) + (nums[k] - query))
        return output

    def binarySearch(self, lo: int, hi: int, nums: List[int], target: int) -> Tuple[int, bool]:
        if lo > hi:
            return lo, False
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid, True
        elif nums[mid] > target:
            return self.binarySearch(lo, mid - 1, nums, target)
        else:
            return self.binarySearch(mid + 1, hi, nums, target)
