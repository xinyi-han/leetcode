class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        copy = x
        reverse = 0
        while x > 0:
            remainder = x % 10
            reverse = reverse * 10 + remainder
            x = x // 10
        return copy == reverse
