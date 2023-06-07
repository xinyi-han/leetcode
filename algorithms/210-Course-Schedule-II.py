from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashMap = dict()
        take = list()
        for course, prereq in prerequisites:
            if course not in hashMap:
                hashMap[course] = set()
            hashMap[course].add(prereq)

        def dfs(c: int, stack: List[int]) -> bool:
            if c in set(stack):
                return False
            stack.append(c)
            if c not in hashMap:
                return True
            for pre in hashMap[c]:
                if pre in set(take):
                    continue
                if not dfs(pre, stack):
                    return False
                pre = stack.pop()
                take.append(pre)
            return True

        for i in range(numCourses):
            if i in set(take):
                continue
            if not dfs(i, []):
                return list()
            take.append(i)
        return take
