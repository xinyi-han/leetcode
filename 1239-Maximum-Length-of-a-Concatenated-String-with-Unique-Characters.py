from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.maxLen = 0
        hashSet = set()

        def dfs(i: int):
            length = len(hashSet)
            if i == len(arr):
                self.maxLen = max(self.maxLen, length)
                return
            for j in range(i, len(arr)):
                for k, char in enumerate(arr[j]):
                    if char in hashSet:
                        self.maxLen = max(self.maxLen, length)
                        for char in arr[j][:k]:
                            hashSet.remove(char)
                        break
                    hashSet.add(char)
                else:
                    dfs(j + 1)
                    for char in arr[j]:
                        hashSet.remove(char)

        dfs(0)
        return self.maxLen
