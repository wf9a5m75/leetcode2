class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orgColor = image[sr][sc]
        if (orgColor == color):
            return image
        M, N = len(image), len(image[0])

        queue = deque( [(sr << 8 | sc)] )
        while (queue):
            pos = queue.popleft()
            y,x = pos >> 8, pos & 0xFF
            if (y < 0) or (x < 0) or (y >= M) or (x >= N):
                continue

            if (image[y][x] == orgColor):
                image[y][x] = color
                queue.append( (y << 8) | (x + 1) )
                queue.append( (y << 8) | (x - 1) )
                queue.append( ((y - 1) << 8) | x )
                queue.append( ((y + 1) << 8) | x )

        return image
