from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordLens = list(map(len, words))
        output = list()
        i = 0
        while i < len(words):
            j = 0
            row = list()
            length = 0
            while i + j < len(words):
                length += wordLens[i + j]
                if length > maxWidth - j:
                    length -= wordLens[i + j]
                    break
                row.append(words[i + j])
                j += 1
            if i + j == len(words):
                s = " ".join(row)
                s += " " * (maxWidth - len(s))
            else:
                diff = maxWidth - length
                if j == 1:
                    s = row[0] + " " * diff
                else:
                    div = diff // (j - 1)
                    mod = diff % (j - 1)
                    spaces = [div for _ in range(j - 1)]
                    for k in range(mod):
                        spaces[k] += 1
                    spaces = [num * " " for num in spaces]
                    spaces.append("")
                    merge = [word + spaces[k] for k, word in enumerate(row)]
                    s = "".join(merge)
            output.append(s)
            i += j
        return output
