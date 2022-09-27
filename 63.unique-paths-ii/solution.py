class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])

        if (obstacleGrid[M - 1][N - 1] == 1):
            return 0

        dp = [[0] * (N + 1) for _ in range(M + 1)]
        dp[0][0] = 1
        for y in range(M):
            for x in range(N):
                if (obstacleGrid[y][x] == 1):
                    continue
                dp[y + 1][x] += dp[y][x]
                dp[y][x + 1] += dp[y][x]
        return dp[M - 1][N - 1]
