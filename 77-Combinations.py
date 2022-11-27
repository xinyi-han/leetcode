from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        prev = 0
        stack = list()
        output = list()
        while True:
            diff = k - len(stack)
            for i in range(prev + 1, prev + 1 + diff):
                stack.append(i)
            output.append(list(stack))
            num = stack.pop()
            for j in range(num + 1, n + 1):
                stack.append(j)
                output.append(list(stack))
                stack.pop()
            if len(stack) == 0:
                break
            while len(stack) > 0:
                num = stack.pop()
                if n - (num + 1) >= k - (len(stack) + 1):
                    prev = num
                    break
            if len(stack) == 0 and num == n - k + 1:
                break
        return output


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = [[i] for i in range(1, n + 1)]
        while len(output[0]) < k:
            temp = list()
            for comb in output:
                num = comb[-1]
                for j in range(num + 1, n + 1):
                    temp.append(comb + [j])
            output = temp
        return output
