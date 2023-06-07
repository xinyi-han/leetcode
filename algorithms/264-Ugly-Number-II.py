import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [(1, (0, 0, 0))]
        heapq.heapify(heap)
        hashSet = {(0, 0, 0)}
        i = 0
        num = 0
        while i < n:
            num, (two, three, five) = heapq.heappop(heap)
            if (two + 1, three, five) not in hashSet:
                hashSet.add((two + 1, three, five))
                heap.append((num * 2, (two + 1, three, five)))
            if (two, three + 1, five) not in hashSet:
                hashSet.add((two, three + 1, five))
                heap.append((num * 3, (two, three + 1, five)))
            if (two, three, five + 1) not in hashSet:
                hashSet.add((two, three, five + 1))
                heap.append((num * 5, (two, three, five + 1)))
            heapq.heapify(heap)
            i += 1
        return num
