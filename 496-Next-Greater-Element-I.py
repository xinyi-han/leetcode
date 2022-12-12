from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = dict()
        for i, num in enumerate(nums2):
            hashMap[num] = i
        output = list()
        for num in nums1:
            i = hashMap[num]
            for j in range(i + 1, len(nums2)):
                if nums2[j] > num:
                    output.append(nums2[j])
                    break
            else:
                output.append(-1)
        return output
