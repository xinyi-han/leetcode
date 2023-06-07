class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        words = [word for word in words if len(word) > 0]
        words.reverse()
        return " ".join(words)
