class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = 0
        cols = 0

        rowMask = 1
        M, N = len(matrix), len(matrix[0])
        for y in range(M):
            colMask = 1
            for x in range(N):
                if matrix[y][x] == 0:
                    rows |= rowMask
                    cols |= colMask
                colMask <<= 1
            rowMask <<= 1

        mask = 1
        for y in range(M):
            if (rows & mask) != 0:
                for x in range(N):
                    matrix[y][x] = 0
            mask <<= 1

        mask = 1
        for x in range(N):
            if (cols & mask) != 0:
                for y in range(M):
                    matrix[y][x] = 0
            mask <<= 1
