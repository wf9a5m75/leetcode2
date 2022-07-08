class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        dp = [[1000000] * N for _ in range(M)]
        for y in range(M):
            for x in range(N):
                if (mat[y][x] == 0):
                    dp[y][x] = 0

                if (y + 1 < M):
                    dp[y + 1][x] = min(dp[y + 1][x], dp[y][x] + 1)
                if (x + 1 < N):
                    dp[y][x + 1] = min(dp[y][x + 1], dp[y][x] + 1)

        for y in range(M - 1, -1, -1):
            for x in range(N - 1, -1, -1):
                if (mat[y][x] == 0):
                    dp[y][x] = 0

                if (0 < y):
                    dp[y - 1][x] = min(dp[y - 1][x], dp[y][x] + 1)
                if (0 < x):
                    dp[y][x - 1] = min(dp[y][x - 1], dp[y][x] + 1)

        return dp
                        
