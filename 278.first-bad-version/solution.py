# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 0
        R = n + 1
        while(L < R):
            mid = (L + R) >> 1
            if isBadVersion(mid):
                R = mid
            else:
                L = mid + 1
        return L
