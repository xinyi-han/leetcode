from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        prev = [set() for _ in range(target + 1)]
        for candidate in candidates:
            curr = list()
            for i, lst in enumerate(prev):
                combs = set(prev[i])  # deep copy
                if candidate == i:
                    combs.add((candidate,))
                elif candidate < i:
                    for tpl in prev[i - candidate]:
                        combs.add(tuple(list(tpl) + [candidate]))
                curr.append(combs)
            prev = curr
        return [list(s) for s in prev[-1]]
