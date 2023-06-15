class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        if str2[:len(str1)] != str1:
            return ""
        x = str1
        for _ in str1:
            if (len(str1) % len(x) == 0 and
                len(str1) // len(x) * x == str1 and
                len(str2) % len(x) == 0 and
                len(str2) // len(x) * x == str2):
                return x
            x = x[:-1]
        return ""
