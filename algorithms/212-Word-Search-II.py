from typing import List


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        self.times = 0

    def add(self, word: str):
        root = self
        root.times += 1
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
            root.times += 1
        root.isEnd = True

    def prune(self, word: str):
        root = self
        root.times -= 1
        for char in word:
            root = root.children[char]
            root.times -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add(word)
        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()
        output = list()

        def dfs(x: int, y: int, node: TrieNode, word: str):
            if node.isEnd:
                output.append(word)
                node.isEnd = False
                root.prune(word)
            for dx, dy in directions:
                X = x + dx
                Y = y + dy
                if 0 <= X < m and 0 <= Y < n and (X, Y) not in visit and board[X][Y] in node.children and node.children[board[X][Y]].times > 0:
                    visit.add((X, Y))
                    letter = board[X][Y]
                    dfs(X, Y, node.children[letter], word + letter)
                    visit.remove((X, Y))

        for r in range(m):
            for c in range(n):
                char = board[r][c]
                if char in root.children and root.children[char].times > 0:
                    visit.add((r, c))
                    dfs(r, c, root.children[char], char)
                    visit.remove((r, c))
        return output
