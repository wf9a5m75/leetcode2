#
# Time complexity: O(M log N)
# Space complexity: O(1)
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)

        y = 0
        result = False
        while (result == False) and (y < M) and (matrix[y][0] <= target):
            result = self._binarySearch(matrix, y, target)
            y += 1
        return result

    def _binarySearch(self, matrix: List[List[int]], y: int, target: int) -> bool:
        N = len(matrix[0])
        if (matrix[y][0] > target) or (matrix[y][N - 1] < target):
            return False

        # find the column
        L = 0
        R = N
        cnt = 0
        while(L < R):
            mid = (L + R) >> 1
            if (matrix[y][mid] == target):
                return True
            elif (matrix[y][mid] < target):
                L = mid + 1
            else:
                R = mid
        return False
