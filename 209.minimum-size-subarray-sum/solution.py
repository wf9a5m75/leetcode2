class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = R = 0
        s = 0
        size = len(nums)
        minL = size + 1
        while(R < size):
            while(s < target) and (R < size):
                s += nums[R]
                R += 1

            while(s >= target):
                s -= nums[L]
                L += 1
            minL = min(minL, R - L + 1)

        return 0 if minL == size + 1 else minL
