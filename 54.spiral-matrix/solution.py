class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        M, N = len(matrix), len(matrix[0])
        start = Point(0, 0)
        end = Point(N - 1, M - 1)
        cnt = M * N

        results = []
        curr = Point(0, 0)
        delta = Point(1, 0)
        while(cnt > 0):
            # print(curr)
            results.append(matrix[ curr.y ][ curr.x ])

            # Heads to down at the right/top
            if (delta.x == 1) and (curr.x == end.x):
                delta.x = 0
                delta.y = 1

            # Heads to left at the right/bottom
            elif (delta.y == 1) and (curr.y == end.y):
                delta.x = -1
                delta.y = 0

            # Heads to up at the left/bottom
            elif (delta.x == -1) and (curr.x == start.x):
                delta.x = 0
                delta.y = -1

            # Heads to right at the left/top
            elif (delta.y == -1) and (curr.y == start.y + 1):
                start.x += 1
                start.y += 1
                end.x -= 1
                end.y -= 1
                delta.x = 1
                delta.y = 0

            curr.y += delta.y
            curr.x += delta.x
            cnt -= 1

        return results
