from typing import List, Tuple


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        self.count = 0

    def buildTrie(self, word: str):
        node = self
        node.count += 1
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.isEnd = True

    def prune(self, word: str):
        node = self
        node.count -= 1
        for char in word:
            node = node.children[char]
            node.count -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.buildTrie(word)

        m = len(board)
        n = len(board[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        output = list() # set()
        visit = set()

        def dfs(pos: Tuple[int, int], node: TrieNode, word: str):
            if node.isEnd:
                output.append(word) # output.add(word)
                # avoid Time Limit Exceeded
                node.isEnd = False
                root.prune(word)
            for dx, dy in directions:
                x, y = pos
                x += dx
                y += dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visit and board[x][y] in node.children and node.children[board[x][y]].count >= 1:
                    visit.add((x, y))
                    char = board[x][y]
                    dfs((x, y), node.children[char], word + char)
                    visit.remove((x, y))

        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in root.children and root.children[char].count >= 1:
                    visit.add((i, j))
                    dfs((i, j), root.children[char], char)
                    visit.remove((i, j))
        return output # list(output)
