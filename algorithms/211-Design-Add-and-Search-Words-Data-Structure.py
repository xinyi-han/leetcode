class WordDictionary:

    def __init__(self):
        self.children = dict()
        self.isWord = False

    def addWord(self, word: str) -> None:
        root = self
        for char in word:
            if char not in root.children:
                root.children[char] = WordDictionary()
            root = root.children[char]
        root.isWord = True

    def search(self, word: str) -> bool:
        root = self
        for i, char in enumerate(word):
            if char != ".":
                if char not in root.children:
                    return False
                root = root.children[char]
            else:
                for k, v in root.children.items():
                    if v.search(word[i + 1:]):
                        return True
                return False
        return root.isWord
