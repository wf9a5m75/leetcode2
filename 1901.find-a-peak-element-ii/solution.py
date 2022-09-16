class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        M, N = len(mat), len(mat[0])

        @cache
        def getVal(y: int, x: int) -> int:
            if (y < 0) or (y >= M) or (x < 0) or (x >= N):
                return -1
            return mat[y][x]

        def binarySearch(y: int, start: int, end: int) -> int:
            L = start
            R = end
            if (L > R):
                return -1
            if (L == R):
                return L if (getVal(y, L - 1) < getVal(y, L) > getVal(y, L + 1)) else -1

            while(L < R):
                mid = (L + R) >> 1
                if (getVal(y, mid) < getVal(y, mid + 1)):
                    L = mid + 1
                else:
                    R = mid

            cell = getVal(y, L)
            isPeak = True
            for dy, dx in directions:
                if (getVal(y + dy, L + dx) > cell):
                    isPeak = False
                    break

            if isPeak:
                return L
            else:
                result = binarySearch(y, start, L - 1)
                if (result == -1):
                    result = binarySearch(y, L + 1, end)
                return result

        for m in range(M):
            result = binarySearch(m, 0, N - 1)
            if (result != -1):
                return [m, result]
            
