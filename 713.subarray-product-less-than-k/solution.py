class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        p = 1
        ans = L = 0
        for R, val in enumerate(nums):
            p *= val
            while (p >= k) and (L <= R):
                p /= nums[L]
                L += 1
            ans += R - L + 1

        return ans
