class Solution:

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])

        def diagnalCheck(x: int, y: int)-> bool:
            val = matrix[y][x]
            while(y < M) and (x < N) and (matrix[y][x] == val):
                y += 1
                x += 1
            return (y == M) or (x == N)


        x = y = 0
        isValid = True
        while (isValid and y < M):
            isValid = diagnalCheck(0, y)
            y += 1
        while (isValid and x < N):
            isValid = diagnalCheck(x, 0)
            x += 1
        return isValid
            
