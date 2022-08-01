class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num == 1):
            return True
        L = 1
        R = num >> 1
        while(L <= R):
            mid = (L + R) >> 1
            dblMid = mid ** 2

            if (dblMid == num):
                return True
            elif (dblMid < num):
                L = mid + 1
            else:
                R = mid - 1
        return False
