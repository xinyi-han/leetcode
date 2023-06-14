class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        i = 0
        output = ""
        while i < length:
            output += word1[i] + word2[i]
            i += 1
        output += word1[length:] + word2[length:]
        return output
