class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        N = len(grid[0])
        for row in grid:
            L = 0
            R = N - 1
            while(L <= R):
                mid = (L + R) >> 1
                if (row[mid] < 0):
                    R = mid - 1
                else:
                    L = mid + 1
            count += N - L
        return count
