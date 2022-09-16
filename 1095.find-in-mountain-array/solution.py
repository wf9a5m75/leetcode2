# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()

        @cache
        def getVal(idx: int) -> int:
            return mountain_arr.get(idx)

        def findThePeak() -> int:
            L = 0
            R = size - 1
            while(L < R):
                mid = (L + R) >> 1
                if (getVal(mid) < getVal(mid + 1)):
                    L = mid + 1
                else:
                    R = mid
            return L

        def binarySearch(L: int, R: int) -> int:
            if (L == R):
                return L if getVal(L) == target else -1
            if (L > R):
                return -1
            while(L < R):
                mid = (L + R) >> 1
                if (getVal(mid) == target):
                    R = mid
                elif (getVal(mid) < target):
                    L = mid + 1
                else:
                    R = mid - 1

            if (getVal(L) == target):
                return L
            elif (R >= 0) and (getVal(R) == target):
                return R
            else:
                return -1

        def binarySearchReverse(L: int, R: int) -> int:
            if (L == R):
                return L if getVal(L) == target else -1
            if (L > R):
                return -1
            while(L < R):
                mid = (L + R) >> 1
                if (getVal(mid) == target):
                    R = mid
                elif (getVal(mid) < target):
                    R = mid - 1
                else:
                    L = mid + 1

            if (getVal(L) == target):
                return L
            elif (R >= 0) and (getVal(R) == target):
                return R
            else:
                return -1

        peak = findThePeak()
        if (getVal(peak) == target):
            return peak
        result = binarySearch(0, peak - 1)

        if (result == -1):
            result = binarySearchReverse(peak + 1, size - 1)
        return result
