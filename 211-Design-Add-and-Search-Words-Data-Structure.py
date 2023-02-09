class Trie:
    def __init__(self):
        self.children = dict()
        self.isWord = False

    def add(self, word: str):
        root = self
        for char in word:
            if char not in root.children:
                root.children[char] = Trie()
            root = root.children[char]
        root.isWord = True

    def search(self, word: str) -> bool:
        root = self
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.isWord


class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        self.root.add(word)

    def search(self, word: str) -> bool:

        def dfs(i: int, root: Trie) -> bool:
            for j in range(i, len(word)):
                char = word[j]
                if char != ".":
                    if char not in root.children:
                        return False
                    root = root.children[char]
                else:
                    for child in root.children:
                        if dfs(j + 1, root.children[child]):
                            return True
                    return False
            return root.isWord

        return dfs(0, self.root)
