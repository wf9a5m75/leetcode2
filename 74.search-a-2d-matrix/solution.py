class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix[0])
        for row in matrix:
            if row[0] <= target <= row[N-1]:
                L = 0
                R = N
                while(L < R):
                    mid = (L + R) >> 1
                    if (row[mid] == target):
                        return True
                    elif (row[mid] < target):
                        L= mid + 1
                    else:
                        R = mid - 1
                # print(L,R)
                return (0 <= L < N) and (row[L] == target)
        return False
