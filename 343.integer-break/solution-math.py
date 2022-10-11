#
# https://leetcode.com/problems/integer-break/discuss/2686750/
#
class Solution:
    def integerBreak(self, n: int) -> int:
        if (n == 2):
            return 1
        if (n == 3):
            return 2

        # q denotes the maximum number of 3
        q = n // 3
        rest = n % 3

        # If the rest could be odd, we need to adjust it until even.
        while((rest & 1) == 1):
            q -= 1
            rest += 3

        return (3 ** q) * (2 ** (rest >> 1))
