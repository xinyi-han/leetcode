from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        output = list()
        heap = list()
        count = 0
        heapq.heappush(heap, (nums1[0] + nums2[0], count, (0, 0)))
        pairs = {(0, 0)}
        while len(heap) > 0 and len(output) < k:
            (_, _, (i, j)) = heapq.heappop(heap)
            output.append([nums1[i], nums2[j]])
            if i == len(nums1) - 1 and j == len(nums2) - 1:
                continue
            elif i == len(nums1) - 1:
                if (i, j+1) in pairs:
                    continue
                count += 1
                heapq.heappush(heap, (nums1[i] + nums2[j+1], count, (i, j+1)))
                pairs.add((i, j+1))
            elif j == len(nums2) - 1:
                if (i+1, j) in pairs:
                    continue
                count += 1
                heapq.heappush(heap, (nums1[i+1] + nums2[j], count, (i+1, j)))
                pairs.add((i+1, j))
            else:
                if (i, j+1) not in pairs:
                    count += 1
                    heapq.heappush(heap, (nums1[i] + nums2[j + 1], count, (i, j + 1)))
                    pairs.add((i, j+1))
                if (i+1, j) not in pairs:
                    count += 1
                    heapq.heappush(heap, (nums1[i + 1] + nums2[j], count, (i + 1, j)))
                    pairs.add((i + 1, j))
        return output
