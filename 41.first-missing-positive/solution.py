class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.append(0)
        N = len(nums)
        for i in range(N):
            if (nums[i] < 0) or (nums[i] >= N):
                nums[i] = 0

        for i in range(N):
            idx = nums[i] % N
            nums[idx] += N

        for i in range(1, N):
            if nums[i] // N == 0:
                return i
        return N
