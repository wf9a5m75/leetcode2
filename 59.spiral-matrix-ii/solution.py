class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        start = Point(0, 0)
        end = Point(n - 1, n - 1)

        result = [
            [0] * n for _ in range(n)
        ]
        last = n * n
        cnt = 1
        curr = Point(0, 0)
        delta = Point(1, 0)

        while(cnt <= last):
            result[curr.y][curr.x] = cnt
            if (delta.x == 1) and (curr.x == end.x):
                # goes down
                delta.x = 0
                delta.y = 1
            elif (delta.y == 1) and (curr.y == end.y):
                # goes left
                delta.x = -1
                delta.y = 0
            elif (delta.x == -1) and (curr.x == start.x):
                # goes up
                delta.x = 0
                delta.y = -1
            elif (delta.y == -1) and (curr.y == start.y + 1):
                # goes right
                delta.x = 1
                delta.y = 0

                start.x += 1
                start.y += 1
                end.x -= 1
                end.y -= 1

            curr.x += delta.x
            curr.y += delta.y
            cnt += 1
        return result
