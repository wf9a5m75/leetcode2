class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        size = len(nums)
        if (size == 1):
            return nums[0]


        dp = [
            nums,
            [0] * size
        ]
        L = 0
        R = size - 1

        prev, curr = 0, 1
        while(L < R):
            for i in range(1, R + 1):
                dp[curr][i - 1] = (dp[prev][i-1] + dp[prev][i]) % 10
            R -= 1
            prev, curr = curr, prev
        return dp[prev][0]
