class TrieNode:
    def __init__(self):
        self.eow = False
        self.word = ""
        self.children = [None] * 26
        self.childCnt = 0

    def __repr__(self):
        _c = []
        for child in self.children:
            _c.append("" if child is None else child)
        return f"'{self.word}':{self.childCnt}:{_c}"

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        M, N = len(board), len(board[0])

        boardChars = 0
        for y in range(M):
            for x in range(N):
                idx = ord(board[y][x]) - 97
                boardChars |= 1 << idx
                board[y][x] = idx


        trie = TrieNode()
        wordChars = 0
        for phrase in words:
            shouldAdd = True
            parent = trie

            indicies = []
            for c in phrase:
                idx = ord(c) - 97
                if (boardChars & (1 << idx)) == 0:
                    shouldAdd = False
                    break
                indicies.append(idx)

            if not shouldAdd:
                continue

            for idx in indicies:
                wordChars |= 1 << idx

                if parent.children[idx] is None:
                    parent.children[idx] = TrieNode()
                parent.childCnt += 1

                parent = parent.children[idx]

            parent.eow = True
            parent.word = phrase
            parent.childCnt += 1

        results = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(parent: TrieNode, x: int, y: int, cnt: int) -> bool:
            idx = board[y][x]
            if (idx < 0):
                return False

            if (wordChars & (1 << idx)) == 0:
                board[y][x] = -1
                return False

            if parent is None:
                return False

            if (parent.eow):
                parent.eow = False
                results.append(parent.word)
                parent.childCnt -= 1
                if parent.childCnt == 0:
                    return True

            cnt += 1

            if cnt == 11:
                return parent.childCnt == 0

            board[y][x] = -1

            for delta in directions:
                dx = x + delta[0]
                dy = y + delta[1]
                if (dx < 0) or (dx == N) or (dy < 0) or (dy == M):
                    continue

                idx2 = board[dy][dx]
                if (idx2 < 0) or (parent.children[idx2] is None):
                    continue

                rc = dfs(parent.children[idx2], dx, dy, cnt)
                if rc:
                    parent.children[idx2] = None
                    parent.childCnt -= 1

            board[y][x] = idx
            return parent.childCnt == 0

        for y in range(M):
            for x in range(N):
                idx = board[y][x]
                if (idx < 0):
                    continue
                if (trie.children[idx] is None):
                    continue

                dfs(trie.children[idx], x, y, 1)
        # print(board)
        return results
