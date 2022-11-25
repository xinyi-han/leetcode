from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = dict()
        for s in strs:
            key = "".join(sorted(s))
            if key not in hashMap:
                hashMap[key] = list()
            hashMap[key].append(s)
        output = list()
        for k, v in hashMap.items():
            output.append(v)
        return output
