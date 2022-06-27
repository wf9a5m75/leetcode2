class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        N = len(nums)

        def backtracking(idx: int, counter: int, prev: int) -> int:
            if (idx == N):
                return counter

            if nums[idx] > prev:
                return backtracking(idx + 1, counter + 1, nums[idx])
            else:
                another = backtracking(idx + 1, 1, nums[idx])
                return max(counter, another)

        return backtracking(0, 0, nums[0] - 1)
