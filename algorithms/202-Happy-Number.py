class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            if n in nums:
                return False
            nums.add(n)
            digits = list(map(int, list(str(n))))
            n = sum(list(map(lambda x: x**2, digits)))
        return True
