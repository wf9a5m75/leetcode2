class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])

        # (1) Flip holizontally
        #  time complexity: O(N * N)
        #  space complexity: O(1)

        for y in range(M):
            L, R = 0, N - 1
            while(L < R):
                matrix[y][L], matrix[y][R] = matrix[y][R], matrix[y][L]
                R -= 1
                L += 1

        # (2) Swap diagonally
        #  time complexity: O(N * N)
        #  space complexity: O(1)

        L = [0, N - 2] # [x, y]
        R = [1, N - 1]
        while(L[1] >= 0):
            self.swapDiagonally(matrix, L[0], L[1], R[0], R[1])
            L[1] -= 1
            R[0] += 1

        L[0] += 1
        L[1] = 0
        R[0] = N - 1
        R[1] -= 1
        while(R[1] > 0):
            self.swapDiagonally(matrix, L[0], L[1], R[0], R[1])
            L[0] += 1
            R[1] -= 1

    def swapDiagonally(self, matrix: List[List[int]], LX: int, LY: int, RX: int, RY: int) -> None:
        if (LY < RY):
            matrix[LY][LX], matrix[RY][RX] = matrix[RY][RX], matrix[LY][LX]
            LX += 1
            LY += 1
            RX -= 1
            RY -= 1
            self.swapDiagonally(matrix, LX, LY, RX, RY)
