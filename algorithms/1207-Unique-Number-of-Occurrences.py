from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = dict()
        for num in arr:
            hashMap[num] = hashMap.get(num, 0) + 1
        return len(set(hashMap.values())) == len(list(hashMap.values()))
