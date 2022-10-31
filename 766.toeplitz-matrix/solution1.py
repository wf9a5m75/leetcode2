class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])

        def checkDiagonal(x: int, y: int) -> bool:
            startVal = matrix[y][x]
            y -= 1
            x -= 1
            while(x >= 0) and (y >= 0):
                if (matrix[y][x] != startVal):
                    return False
                y -= 1
                x -= 1
            return True

        for x in range(N):
            if checkDiagonal(x, M - 1) == False:
                return False

        for y in range(M):
            if checkDiagonal(N - 1, y) == False:
                return False
        return True
