from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = set()
        dictionary.sort()
        for root in dictionary:
            for i in range(1, len(root)):
                if root[:i] in trie:
                    break
            else:
                trie.add(root)
        maxLen = max(list(map(len, trie)))
        words = sentence.split()
        for i, word in enumerate(words):
            for j in range(1, min(maxLen, len(word)) + 1):
                if word[:j] in trie:
                    words[i] = word[:j]
                    break
        return " ".join(words)
