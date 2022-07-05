class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        nearest = 999999999999
        position = -1
        for i, point in enumerate(points):
            if (x == point[0]) or (y == point[1]):
                distance = abs(x - point[0]) + abs(y - point[1])
                if nearest > distance:
                    nearest = distance
                    position = i
        return position
