#https://leetcode.com/problems/find-k-closest-elements/discuss/1310981/Simple-Solutions-w-Explanation-or-All-Possible-Approaches-Explained!

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        L = 0
        R = size - k
        while(L < R):
            mid = (L + R) >> 1
            if (arr[mid] == arr[mid + k]):
                if (arr[mid] < x):
                    L = mid + 1
                else:
                    R = mid
            elif (abs(x - arr[mid]) <= abs(x - arr[mid + k])):
                R = mid
            else:
                L = mid + 1
        return arr[L : L + k]
