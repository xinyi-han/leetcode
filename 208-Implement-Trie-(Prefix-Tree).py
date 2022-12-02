class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        for i, char in enumerate(word):
            substring = word[:i]
            if substring not in self.trie:
                self.trie[substring] = set()
            self.trie[substring].add(char)
        if word not in self.trie:
            self.trie[word] = set()
        self.trie[word].add("")

    def search(self, word: str) -> bool:
        return word in self.trie and "" in self.trie[word]

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.trie
