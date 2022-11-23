from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = [list() for _ in range(target + 1)]
        for candidate in candidates:
            for i, sum in enumerate(combination):
                if candidate > i:
                    continue
                elif candidate == i:
                    sum.append([candidate])
                else:
                    lst = combination[i - candidate]
                    for l in lst:
                        sum.append(l + [candidate])
        return combination[-1]
