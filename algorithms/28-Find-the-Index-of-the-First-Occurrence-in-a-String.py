class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack):
            j = 0
            if haystack[i] == needle[j]:
                while j < len(needle) and i + j < len(haystack) and haystack[i + j] == needle[j]:
                    j += 1
                if j == len(needle):
                    return i
            i += 1
        return -1
