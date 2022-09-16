class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        L = 0
        R = len(arr) - 1
        while(L + 1 < R):
            mid = (L + R) >> 1
            if (arr[mid - 1] < arr[mid] > arr[mid + 1]):
                return mid
            elif (arr[mid - 1] < arr[mid]):
                L = mid + 1
            else:
                R = mid - 1
        if (arr[L] > arr[R]):
            return L
        else:
            return R
