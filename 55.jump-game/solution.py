class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if (len(nums) == 1):
            return True

        maxJump = 0
        for i, num in enumerate(nums):
            maxJump = max(maxJump, i + num)
            if maxJump == i:
                return maxJump == len(nums) - 1
        return True
