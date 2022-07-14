import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n <= 0):
            return False
        s = math.log2(n)
        return int(s) == s
