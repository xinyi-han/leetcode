class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        words = s.split()
        return len(words[-1])
