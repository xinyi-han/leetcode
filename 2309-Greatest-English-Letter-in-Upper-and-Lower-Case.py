class Solution:
    def greatestLetter(self, s: str) -> str:
        chars = set(s)
        letters = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g',
                   'f', 'e', 'd', 'c', 'b', 'a']
        for letter in letters:
            if letter in chars and letter.upper() in chars:
                return letter.upper()
        return ""
