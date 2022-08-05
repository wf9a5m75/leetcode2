class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        dp = [0] * (target + 1)

        # The case total becomes 0 is only 1 (nothing add)
        dp[0] = 1

        for total in range(1, target + 1):
            for num in nums:
                if total - num >= 0:
                    dp[total] += dp[total - num]
                else:
                    break
        return dp[target]
