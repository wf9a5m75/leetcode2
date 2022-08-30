class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (matrix[0][0] > target) or (matrix[-1][-1] < target):
            return False

        # Start from right-top corner
        y, x = 0, len(matrix[0]) - 1
        M = len(matrix)
        while(x >= 0 and y < M):
            if (matrix[y][x] == target):
                return True
            elif (matrix[y][x] > target):
                x -= 1
            else:
                y += 1

        return False
