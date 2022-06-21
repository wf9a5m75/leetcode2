class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [0] * (rowIndex + 1)
        triangle[0] = 1

        startX = rowIndex - 1
        for y in range(rowIndex + 2):
            left = 0
            for x in range(y):
                storeL = triangle[x]
                triangle[x] = left + triangle[x]
                left = storeL
        return triangle
