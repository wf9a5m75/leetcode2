class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        N1 = N + 1
        dp = [[0] * N1 for _ in range(2)]
        currIdx, nextIdx = 0, 1

        result = 0
        for y in range(M):
            for x in range(N):
                dp[nextIdx][x + 1] = 0
                if nums1[y] == nums2[x]:
                    dp[nextIdx][x + 1] = dp[currIdx][x] + 1
                    if (result < dp[nextIdx][x + 1]):
                        result = dp[nextIdx][x + 1]
            currIdx = (currIdx + 1) & 1
            nextIdx = (nextIdx + 1) & 1

        return result
