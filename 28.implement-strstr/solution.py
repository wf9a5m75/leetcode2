#
# DP approach
#  time complexity: O( len(haystack) * len(needle) )
#  space complexity: O( len(haystack) )
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        sizeN = len(needle)
        sizeH = len(haystack)
        dp = [[0] * (sizeH + 1) for _ in range(2)]

        currIdx = 0
        nextIdx = 1
        for i in range(sizeN):
            for j in range(sizeH):
                if (needle[i] == haystack[j]):
                    dp[nextIdx][j + 1] = dp[currIdx][j] + 1
                    if dp[nextIdx][j + 1] == sizeN:
                        # print(dp[nextIdx])
                        return j - sizeN + 1
                else:
                    dp[nextIdx][j + 1] = 0

            # print(dp[nextIdx])
            currIdx, nextIdx = nextIdx, currIdx
        return -1
