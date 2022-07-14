class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])


        # Parse the current status
        fresh = set()
        rotten = []
        for y in range(M):
            for x in range(N):
                cell = grid[y][x]

                if (cell == 2):
                    rotten.append((x, y))
                elif (cell == 1):
                    fresh.add((x, y))


        #
        # BFS Search
        #

        # print(rotten)
        turn = 0
        while(rotten) and (len(fresh) > 0):

            turn += 1
            nextQ = []
            while(rotten) and (len(fresh) > 0):
                x, y = rotten.pop()

                for dx, dy in ([-1, 0], [1, 0], [0, 1], [0, -1]):
                    posY = y + dy
                    posX = x + dx
                    if (0 <= posY < M) and (0 <= posX < N) and grid[posY][posX] == 1:
                        newRotten = (posX, posY)
                        nextQ.append(newRotten)
                        fresh.remove(newRotten)
                        grid[posY][posX] = 2

            rotten = nextQ
            # print(rotten)

        if (len(fresh) > 0):
            return -1
        else:
            return turn
