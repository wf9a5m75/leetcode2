class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)

        s = N - 1
        total = 0
        for p in range(N)
            total += mat[p][p]
            mat[p][p] = 0
            total += mat[p][s]

            p += 1
            s -= 1

        return total
        
