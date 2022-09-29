class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        case1 = nums[-3] * nums[-2] * nums[-1]
        case2 = nums[0] * nums[1] * nums[-1]
        return max(case1, case2)
