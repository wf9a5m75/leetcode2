class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (target < matrix[0][0]) or (target > matrix[-1][-1]):
            return False

        # Find the row
        T = 0
        B = len(matrix) - 1
        if (T == B):
            T = 0
        else:
            while(T <= B):
                mid = (T + B) >> 1
                if (matrix[mid][-1] == target):
                    return True
                elif (matrix[mid][-1] < target):
                    T = mid + 1
                else:
                    B = mid - 1
        # Find in the row
        L = 0
        R = len(matrix[T]) - 1
        if (L != R):
            while(L <= R):
                mid = (L + R) >> 1
                if (matrix[T][mid] == target):
                    return True
                elif (matrix[T][mid] < target):
                    L = mid + 1
                else:
                    R = mid - 1
        return (R < len(matrix[T])) and (matrix[T][R] == target)
