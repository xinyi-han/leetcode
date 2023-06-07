from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        odd = dict()
        even = dict()
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even[num] = even.get(num, 0) + 1
            else:
                odd[num] = odd.get(num, 0) + 1
        oddPairs = [(v, k) for k, v in odd.items()]
        oddPairs.sort(reverse=True)
        oddNum = sum(odd.values())
        evenPairs = [(v, k) for k, v in even.items()]
        evenPairs.sort(reverse=True)
        evenNum = sum(even.values())
        if oddPairs[0][1] != evenPairs[0][1]:
            return (oddNum - oddPairs[0][0]) + (evenNum - evenPairs[0][0])
        if len(oddPairs) == 1 and len(evenPairs) == 1:
            return min(oddPairs[0][0], evenPairs[0][0])
        if len(oddPairs) == 1:
            return evenNum - evenPairs[1][0]
        if len(evenPairs) == 1:
            return oddNum - oddPairs[1][0]
        return min(((oddNum - oddPairs[0][0]) + (evenNum - evenPairs[1][0])),
                   ((oddNum - oddPairs[1][0]) + (evenNum - evenPairs[0][0])))