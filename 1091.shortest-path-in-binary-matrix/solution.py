class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if (grid[0][0] == 1) or (grid[N - 1][N - 1] == 1):
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        q = [(0, 0)]
        cnt = 0
        while(q):
            nextQ = []
            while(q):
                x, y = q.pop(0)
                if (x == N - 1) and (y == N - 1):
                    return cnt + 1

                for dx, dy in directions:
                    dx += x
                    dy += y
                    if (0 <= dx < N) and (0 <= dy < N) and (grid[dy][dx] == 0):
                        nextQ.append((dx, dy))
                        grid[dy][dx] = 1
            q = nextQ
            cnt += 1
        return -1
