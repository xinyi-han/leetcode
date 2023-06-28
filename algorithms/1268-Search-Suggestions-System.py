from typing import List


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for product in products:
            r = root
            for char in product:
                if char not in r.children:
                    r.children[char] = TrieNode()
                r = r.children[char]
            r.isEnd = True
        output = list()
        for i in range(len(searchWord)):
            prefix = searchWord[:i + 1]
            res = self.search(prefix, root)
            output.append(res)
        return output

    def search(self, prefix: str, root: TrieNode) -> List[str]:
        output = list()
        stack = list()
        for char in prefix:
            if char not in root.children:
                return output
            stack.append(char)
            root = root.children[char]

        def dfs(r: TrieNode) -> bool:
            if r.isEnd:
                output.append("".join(stack))
            if len(output) == 3:
                return True
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char in r.children:
                    stack.append(char)
                    if dfs(r.children[char]):
                        return True
                    stack.pop()
            return False

        dfs(root)
        return output
