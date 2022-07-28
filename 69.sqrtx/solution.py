class Solution:
    def mySqrt(self, x: int) -> int:
        if (x < 2):
            return x
        L = 1
        R = x >> 1
        while(L <= R):
            mid = (L + R) >> 1
            if (mid ** 2 <= x):
                L = mid + 1
            else:
                R = mid - 1
        return R
