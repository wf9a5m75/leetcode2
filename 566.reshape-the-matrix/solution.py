class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        columns = len(mat[0])

        if (rows * columns != r * c):
            return mat

        result = [
            [0] * c for _ in range(r)
        ]

        pwriteX = 0
        pwriteY = 0
        idx = 0
        for y in range(rows):
            for x in range(columns):
                # print("({},{}) => ({},{})".format(y, x, pwriteY, pwriteX))
                result[pwriteY][pwriteX] = mat[y][x]
                idx += 1
                pwriteX = idx % c
                pwriteY += 1 if (idx % c == 0) else 0
        return result
