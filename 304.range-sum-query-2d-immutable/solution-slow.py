class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        columns = len(matrix[0])

        self.dp = [[0] * columns for _ in range(rows)]

        for y in range(rows):
            prev = 0
            for x in range(columns):
                self.dp[y][x] = prev + matrix[y][x]
                prev = self.dp[y][x]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for y in range(row1, row2 + 1):
            result += self.dp[y][col2]

        if (col1 > 0):
            for y in range(row1, row2 + 1):
                result -= self.dp[y][col1 - 1]
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
