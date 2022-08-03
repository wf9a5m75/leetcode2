class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])

        if (target < matrix[0][0]) or (target > matrix[M - 1][N - 1]):
            return False

        # Find the row which probably include the target value
        top = 0
        bottom = M - 1
        while(top <= bottom):
            mid = (top + bottom) >> 1
            if (matrix[mid][0] <= target <= matrix[mid][N - 1]):
                top = bottom = mid
                break
            elif (target < matrix[mid][0]):
                bottom = mid - 1
            else:
                top = mid + 1

        if (top == bottom):
            row = matrix[top]
        else:
            if (0 <= bottom) and (matrix[bottom][0] <= target <= matrix[bottom][N - 1]):
                row = matrix[bottom]
            elif (top < M) and (matrix[top][0] <= target <= matrix[top][N - 1]):
                row = matrix[top]
            else:
                return False

        # Find the target in the row
        L = 0
        R = N - 1
        while(L <= R):
            mid = (L + R) >> 1
            if (row[mid] == target):
                return True
            elif (row[mid] < target):
                L = mid + 1
            else:
                R = mid - 1

        return (0 <= L < N) and (row[L] == target)
