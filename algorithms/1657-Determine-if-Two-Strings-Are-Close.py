class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1Map = dict()
        word2Map = dict()
        for char in word1:
            word1Map[char] = word1Map.get(char, 0) + 1
        for char in word2:
            word2Map[char] = word2Map.get(char, 0) + 1
        return (sorted(list(word1Map.values())) == sorted(list(word2Map.values()))
                and set(word1Map.keys()) == set(word2Map.keys()))
