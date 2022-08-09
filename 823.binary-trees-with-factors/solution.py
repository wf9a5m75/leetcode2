class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()

        indexTbl = {}
        for i, val in enumerate(arr):
            indexTbl[val] = i

        dp = [1] * len(arr)

        for i, num1 in enumerate(arr):
            for j in range(i + 1):
                if (num1 % arr[j] == 0):
                    num2 = num1 / arr[j]
                    if (num2 in indexTbl):
                        dp[i] += dp[j] * dp[indexTbl[num2]]
                        dp[i] %= MOD
        return sum(dp) % MOD

            
