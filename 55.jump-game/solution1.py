class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        maxJump = 0

        for i, jmp in enumerate(nums):
            maxJump = max(maxJump, i + jmp)
            if maxJump >= N - 1:
                return True

            if maxJump == i:
                return False
        return False
