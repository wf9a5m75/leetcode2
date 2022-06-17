# Two pointer approach
#
#   time complexity: O(N)
#   space complexity: O(N)
#
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        L, R = 0, len(nums) - 1
        k = len(nums) - 1
        while(L <= R):
            if (abs(nums[L]) > abs(nums[R])):
                ans[k] = nums[L] ** 2
                L += 1
            else:
                ans[k] = nums[R] ** 2
                R -= 1
            k -= 1
        return ans
