class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0

        maxJmp = 0
        nextJmp = 0
        result = 0
        for i, jmp in enumerate(nums):
            nextJmp = max(nextJmp, i + jmp)
            if (i == maxJmp):
                maxJmp = nextJmp
                result += 1
                if (maxJmp >= N - 1):
                    break
        return result
