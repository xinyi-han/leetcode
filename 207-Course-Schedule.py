from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = dict()
        take = set()
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
                if pre in take:
                    continue
                if not dfs(pre, stack):
                    return False
                pre = stack.pop()
                take.add(pre)
            return True

        for i in range(numCourses):
            if i in take:
                continue
            if not dfs(i, []):
                return False
            take.add(i)
        return True
