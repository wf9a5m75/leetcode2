class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        columnMax = [0] * N
        rowMin = [1000000] * M

        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                columnMax[x] = max(columnMax[x], val)
                rowMin[y] = min(rowMin[y], val)

        # find the duplicated values
        return list(set(rowMin) & set(columnMax))

        
