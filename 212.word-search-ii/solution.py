class TrieNode:
    def __init__(self):
        self.eow = False
        self.word = ""
        self.children = {}
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for phrase in words:
            parent = trie
            for c in phrase:
                if c not in parent.children:
                    parent.children[c] = TrieNode()
                parent = parent.children[c]
            parent.eow = True
            parent.word = phrase

        M, N = len(board), len(board[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        results = []
        def dfs(parent: TrieNode, x: int, y: int):
            if (parent.eow):
                parent.eow = False
                results.append(parent.word)

            board[y][x] += ":"
            for dx, dy in directions:
                dx += x
                dy += y
                if (0 <= dx < N) and (0 <= dy < M) and (board[dy][dx] in parent.children):
                    dfs(parent.children.get(board[dy][dx]), dx, dy)

            board[y][x] = board[y][x][0]

        for y in range(M):
            for x in range(N):
                if (board[y][x] in trie.children):
                    dfs(trie.children.get(board[y][x]), x, y)

        return results
