class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = {}
        islandIdx = 1

        def findParent(x: int) -> int:
            startX = x
            while(islands[x] != x):
                x = islands[x]
            return x

        M, N = len(grid), len(grid[0])
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for y in range(M):
            for x in range(N):
                if grid[y][x] == "1":
                    upIdx = dp[y][x + 1]
                    leftIdx = dp[y + 1][x]

                    if (upIdx > 0) and (leftIdx > 0):
                        if (upIdx == leftIdx):
                            idx = upIdx
                        else:
                            # Union two regions, then create a new island index
                            rootA = findParent(upIdx)
                            rootB = findParent(leftIdx)
                            islands[rootA] = islandIdx
                            islands[rootB] = islandIdx
                            islands[islandIdx] = islandIdx
                            idx = islandIdx

                            islandIdx += 1
                    elif (upIdx > 0):
                        idx = upIdx
                    elif (leftIdx > 0):
                        idx = leftIdx
                    else:
                        # found a new region
                        islands[islandIdx] = islandIdx
                        idx = islandIdx
                        islandIdx += 1

                    dp[y + 1][x + 1] = idx
        cnt = 0
        for key in islands.keys():
            cnt += 1 if islands[key] == key else 0

        return cnt
