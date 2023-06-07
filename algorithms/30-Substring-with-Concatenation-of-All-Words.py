from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        wordNum = len(words)
        output = list()
        hashMap = dict()
        for word in words:
            hashMap[word] = hashMap.get(word, 0) + 1
        i = 0
        while i < len(s) - wordLen * wordNum + 1:
            copy = dict(hashMap)
            j = 0
            while i + j < len(s):
                word = s[i + j: i + j + wordLen]
                if word not in copy:
                    break
                else:
                    num = copy[word]
                    if num == 0:
                        break
                    else:
                        copy[word] = num - 1
                j += wordLen
            nums = [v for k, v in copy.items()]
            if len(set(nums)) == 1 and 0 in nums:
                output.append(i)
            i += 1
        return output
