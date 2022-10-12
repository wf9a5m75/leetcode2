class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        size = len(nums)
        if (size < 3):
            return 0

        result = 0
        cnt = prevCnt = 0
        prevDiff = nums[0] - nums[1]
        for i in range(2, size):
            diff = nums[i - 1] - nums[i]
            if prevDiff == diff:
                cnt += 1
            else:
                result += (cnt * (cnt + 1)) >> 1
                cnt = 0
            prevDiff = diff
        result += (cnt * (cnt + 1)) >> 1
        return result
