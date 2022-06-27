class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        m, n = len(grid), len(grid[0])

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 0:
                    continue
                if (y == 0) or (grid[y - 1][x] == 0):
                    perimeter += 2
                if (x == 0) or (grid[y][x - 1] == 0):
                    perimeter += 2
        return perimeter
