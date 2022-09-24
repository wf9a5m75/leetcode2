class Solution:
    def dfs(self, board: List[List[str]], y: int, x: int) -> None:
        q = [(y, x)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        M, N = len(board),len(board[0])

        while(q):
            y, x = q.pop(0)
            if (board[y][x] == "O"):
                board[y][x] = "T"

                for dy, dx in directions:
                    if (0 <= y + dy < M) and (0 <= x + dx < N) and (board[y + dy][x + dx] == "O"):
                        q.append((y + dy, x + dx))



    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


        M, N = len(board),len(board[0])
        for y in range(M):
            self.dfs(board, y, 0)
            self.dfs(board, y, N - 1)

        for x in range(N):
            self.dfs(board, 0, x)
            self.dfs(board, M - 1, x)

        for y in range(M):
            for x in range(N):
                if board[y][x] == "O":
                    board[y][x] = "X"
                elif board[y][x] == "T":
                    board[y][x] = "O"
