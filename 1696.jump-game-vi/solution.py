class ScoreIdx:
    def __init__(self, score: int, idx: int):
        self.score = score
        self.index = idx

    def __repr__(self) -> str:
        return f"\{score:{self.score}, index:{self.index} \}"

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        size = len(nums)
        dp = [0] * size
        dp[0] = nums[0]

        # The q keeps the largest score index at the most left
        q = [ScoreIdx(nums[0], 0)]

        for i in range(1, size):

            # Since the q[0] keeps the largest score always,
            # we can calculate the max score at i
            dp[i] = nums[i] + q[0].score

            # Remove lower scores than dp[i]
            while q and q[-1].score < dp[i]:
                q.pop()

            # Push the largetst score
            q.append(ScoreIdx(dp[i], i))

            # If q[0].index == i - k,
            # we can't use it anymore.
            if i - k == q[0].index:
                q.pop(0)

        return dp[size - 1]
            
