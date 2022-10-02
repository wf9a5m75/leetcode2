class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        MOD = 1000000007

        dp = [[0] * (target + 1) for _ in range(n + 1)]

        dp[n][target] = 1
        for times in range(n - 1, -1, -1):
            for prevSum in range(1, target + 1):
                for diceNum in range(1, k + 1):
                    if prevSum - diceNum >= 0:
                        dp[times][prevSum - diceNum] += dp[times + 1][prevSum]
                        dp[times][prevSum - diceNum] %= MOD
        return dp[0][0]

print(Solution().numRollsToTarget(30, 30, 500) == 222616187)
