class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        M = len(triangle)
        N = len(triangle[M - 1])
        dp = [
            [10 ** 5] * N for _ in range(2)
        ]
        currIdx = 0
        nextIdx = 1

        dp[currIdx][0] = triangle[0][0]

        # print(dp[currIdx])
        for y in range(M - 1):
            for x in range(y + 1):
                dp[nextIdx][x] = min(dp[nextIdx][x], dp[currIdx][x] + triangle[y + 1][x])
                if (x < len(triangle[y])):
                    dp[nextIdx][x + 1] = dp[currIdx][x] + triangle[y + 1][x + 1]
            currIdx, nextIdx = nextIdx, currIdx

            for x in range(y + 1):
                dp[nextIdx][x] = 10 ** 5
            # print(dp[currIdx])

        return min(dp[currIdx])
