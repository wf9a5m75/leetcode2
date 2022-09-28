class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board),len(board[0])
        size = len(word)

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def backtrack(i: int, y: int, x: int) -> bool:
            if board[y][x] == word[i]:
                if i == size - 1:
                    return True

                board[y][x] += ":"
                for dx, dy in directions:
                    dx = x + dx
                    dy = y + dy
                    if ((0 <= dx < N) and (0 <= dy < M) and
                        (board[dy][dx] == word[i + 1]) and backtrack(i + 1, dy, dx)):
                        return True

                board[y][x] = board[y][x][0]
                return False
            else:
                return False

        for y in range(M):
            for x in range(N):
                if (board[y][x] == word[0]) and backtrack(0, y, x):
                    return True
        return False
