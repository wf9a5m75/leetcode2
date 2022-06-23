class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        columns = len(matrix[0])
        columns1 = columns + 1
        rows1 = rows + 1

        self.dp = [[0] * columns1 for _ in range(rows1)]

        for y in range(rows):
            for x in range(columns):
                self.dp[y + 1][x + 1] = matrix[y][x] + self.dp[y][x + 1] + self.dp[y + 1][x] - self.dp[y][x]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rightBottom = self.dp[row2 + 1][col2 + 1]
        upper = self.dp[row1][col2 + 1]
        left = self.dp[row2 + 1][col1]
        leftTop = self.dp[row1][col1]

        return rightBottom - upper - left + leftTop


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
