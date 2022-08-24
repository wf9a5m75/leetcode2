#
# 3**19 is the largest number under 2**31 - 1
#
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return (n > 0) and (3**19 % n == 0)
