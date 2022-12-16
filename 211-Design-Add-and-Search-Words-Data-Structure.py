class WordDictionary:

    def __init__(self):
        self.words = dict()

    def addWord(self, word: str) -> None:
        for i, char in enumerate(word):
            prefix = word[:i]
            if prefix not in self.words:
                self.words[prefix] = set()
            self.words[prefix].add(char)
        if word not in self.words:
            self.words[word] = set()
        self.words[word].add("")

    def search(self, word: str) -> bool:
        if word.isalpha():
            if word not in self.words:
                return False
            return "" in self.words[word]
        dots = [i for i, char in enumerate(word) if char == "."]

        def backtrack(i: int, s: str) -> bool:
            if i == len(dots):
                suffix = word[dots[-1] + 1:]
                if s + suffix in self.words and "" in self.words[s + suffix]:
                    return True
                return False
            if i == 0:
                j = 0
            else:
                j = dots[i - 1] + 1
            prefix = s + word[j:dots[i]]
            if prefix not in self.words:
                return False
            for char in self.words[prefix]:
                if char == "":
                    continue
                if backtrack(i + 1, prefix + char):
                    return True
            return False

        return backtrack(0, "")
