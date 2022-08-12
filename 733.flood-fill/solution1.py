class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]
        if (startColor == color):
            return image

        q = [(sr, sc)]  # (y, x)
        M, N = len(image), len(image[0])

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while(q):
            y, x = q.pop(0)
            hashPos = (y << 7) + x

            if image[y][x] == startColor:
                image[y][x] = color

                for move in moves:
                    y2 = y + move[0]
                    x2 = x + move[1]
                    if (0 <= y2 < M) and (0 <= x2 < N) and (image[y2][x2] == startColor):
                        q.append((y2, x2))
        return image
