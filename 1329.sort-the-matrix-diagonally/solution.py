class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])

        def getValues(x: int, y: int) -> List[int]:
            if (x == N) or (y == M):
                return []
            result = getValues(x + 1, y + 1)
            result.append(mat[y][x])
            return result

        def setValues(x: int, y: int, values: List[int]) -> List[int]:
            if (x == N) or (y == M):
                return
            mat[y][x] = values.pop(0)
            setValues(x + 1, y + 1, values)


        startX = 0
        for startY in range(M - 1, -1, -1):
            values = getValues(startX, startY)
            values.sort()
            setValues(startX, startY, values)

        for startX in range(1, N):
            values = getValues(startX, startY)
            values.sort()
            setValues(startX, startY, values)

        return mat
            
