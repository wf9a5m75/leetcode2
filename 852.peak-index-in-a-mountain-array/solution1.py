class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        L = 0
        R = len(arr) - 1
        while(L < R):
            mid = (L + R) >> 1
            if (arr[mid] < arr[mid + 1]):
                L = mid + 1
            else:
                R = mid
        return L
