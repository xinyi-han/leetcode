from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hashMap = dict()
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        hashSet = set(nums)
        output = [[num] for num in hashSet]
        while len(output[0]) != len(nums):
            temp = set()
            for comb in output:
                copy = dict(hashMap)
                for num in comb:
                    copy[num] -= 1
                    if copy[num] == 0:
                        copy.pop(num)
                for num in copy:
                    temp.add(tuple(comb + [num]))
            temp = [list(tpl) for tpl in temp]
            output = temp
        return output
