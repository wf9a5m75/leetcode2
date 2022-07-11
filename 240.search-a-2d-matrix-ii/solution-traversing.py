#
# Time complexity: O(M + N)
# Space complexity: O(1)
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])

        currY = M - 1
        currX = 0

        while(currY >= 0) and (currX < N):
            currVal = matrix[currY][currX]

            if (currVal == target):
                return True
            elif (currVal < target):
                currX += 1
            elif (currVal > target):
                currY -= 1
            else:
                # We don't go (currY += 1) or (currX -= 1)
                # Because there is no posibility
                return False
        return False
