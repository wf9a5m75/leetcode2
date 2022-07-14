class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        M = len(triangle)
        N = len(triangle[M - 1])
        dp = [
            [10 ** 5] * N for _ in range(2)
        ]
        currIdx = 0
        prevIdx = 1

        dp[currIdx] = triangle[M - 1]

        # print(dp[currIdx])
        for y in range(M - 1, 0, -1):
            for x in range(y):
                dp[prevIdx][x] = min(dp[currIdx][x] + triangle[y - 1][x], dp[currIdx][x + 1] + triangle[y - 1][x])
            currIdx, prevIdx = prevIdx, currIdx

            # print(dp[currIdx])

        return dp[currIdx][0]
