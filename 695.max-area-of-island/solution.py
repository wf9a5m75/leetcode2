class Solution:
    def traverseIsland(self, grid: List[List[int]], startY: int, startX: int) -> int:
        result = 0
        M = len(grid)
        N = len(grid[0])
        queue = [startY << 8 | startX]
        checked = set()

        def addPosition(y: int, x: int) -> None:
            if (0 <= y < M) and (0 <= x < N):
                pos = (y << 8) | x
                if (pos not in checked):
                    checked.add(pos)
                    queue.append(pos)


        while(queue):
            curr = queue.pop(0)

            y, x = curr >> 8, curr & 0xFF
            if (grid[y][x] != 1):
                continue
            grid[y][x] = -1

            result += 1

            addPosition(y - 1, x)
            addPosition(y + 1, x)
            addPosition(y, x - 1)
            addPosition(y, x + 1)

        return result



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        M = len(grid)
        N = len(grid[0])

        for y in range(M):
            for x in range(N):
                if grid[y][x] == 1:
                    result = max(result, self.traverseIsland(grid, y, x))
        return result
