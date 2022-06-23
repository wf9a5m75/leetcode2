class NumArray:

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.dp = [0] * self.size

        prev = 0
        for i in range(self.size):
            self.dp[i] = prev + nums[i]
            prev = self.dp[i]

    def sumRange(self, left: int, right: int) -> int:
        result = self.dp[right]

        leftSum = 0
        if (left > 0):
            leftSum = self.dp[left - 1]

        return result - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
