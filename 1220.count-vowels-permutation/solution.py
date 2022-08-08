class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if (n == 1):
            return 5

        MOD = 1000000007

        charA = 0
        charE = 1
        charI = 2
        charO = 3
        charU = 4

        dp = [
            [1,1,1,1,1],  # base case
            [0,0,0,0,0]
        ]

        prevIdx = 0
        currIdx = 1
        for i in range(n - 1):

            dp[currIdx][charA] = (dp[prevIdx][charE] + dp[prevIdx][charI] + dp[prevIdx][charU]) % MOD
            dp[currIdx][charE] = (dp[prevIdx][charA] + dp[prevIdx][charI]) % MOD
            dp[currIdx][charI] = (dp[prevIdx][charE] + dp[prevIdx][charO]) % MOD
            dp[currIdx][charO] = (dp[prevIdx][charI]) % MOD
            dp[currIdx][charU] = (dp[prevIdx][charI] + dp[prevIdx][charO]) % MOD

            prevIdx, currIdx = currIdx, prevIdx

        return sum(dp[prevIdx]) % MOD
        
