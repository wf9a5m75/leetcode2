#
# This question is extended from https://leetcode.com/problems/longest-increasing-subsequence/
#
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dpLen = [1] * N
        dpCnt = [1] * N

        for i in range(N):
            for j in range(i):
                if (nums[j] < nums[i]):
                    if (dpLen[i] < dpLen[j] + 1):
                        dpLen[i] = dpLen[j] + 1
                        dpCnt[i] = dpCnt[j]

                    elif (dpLen[i] == dpLen[j] + 1):
                        dpCnt[i] += dpCnt[j]

        maxLen = 0
        maxCnt = 0
        for i in range(N):
            if maxLen < dpLen[i]:
                maxLen = dpLen[i]
                maxCnt = dpCnt[i]

            elif (maxLen == dpLen[i]):
                maxCnt += dpCnt[i]

        # print(dpLen)
        # print(dpCnt)
        return maxCnt
