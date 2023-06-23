from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        while j < len(chars):
            k = 1
            while j + k < len(chars) and chars[j] == chars[j + k]:
                k += 1
            chars[i] = chars[j]
            i += 1
            j += k
            if k > 1:
                k = str(k)
                for m, s in enumerate(k):
                    chars[i + m] = s
                i += len(k)
        return i
