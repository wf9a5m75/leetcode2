class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s
        rows = [[] for _ in range(numRows)]

        dy = 1
        y = 0
        for char in s:
            rows[y].append(char)
            y += dy
            if (y == numRows):
                dy = -1
                y = numRows - 2
            elif (y == -1):
                dy = 1
                y = 1

        result = ""
        for row in rows:
            result += "".join(row)
        return result
