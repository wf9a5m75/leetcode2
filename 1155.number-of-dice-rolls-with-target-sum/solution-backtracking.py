from functools import cache

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        MOD = 1000000007

        @cache
        def backtrack(i: int, target: int) -> int:
            if (i == 0):
                if (target == 0):
                    return 1
                else:
                    return 0

            result = 0
            for j in range(1, k + 1):
                tmp = target - j
                if tmp >= 0:
                    result = (result + backtrack(i - 1, tmp)) % MOD
                else:
                    break
            return result

        return backtrack(n, target)

print(Solution().numRollsToTarget(30, 30, 500) == 222616187)
