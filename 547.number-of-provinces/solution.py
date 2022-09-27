class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)

        dp = [0] * N
        provinces = {0: 0}
        provIdx = 0

        def findParent(x: int) -> int:
            p = provinces[x]
            if p == x:
                return p
            provinces[x] = findParent(p)
            return provinces[x]

        for y in range(N):
            for x in range(N):
                if isConnected[y][x] == 0:
                    continue

                p1 = findParent(dp[y])
                p2 = findParent(dp[x])

                if (p1 + p2 == 0):
                    # both groups are not labeled yet.
                    provIdx += 1
                    provinces[provIdx] = provIdx
                    dp[y] = dp[x] = provIdx
                elif (p1 == 0) or (p2 == 0):
                    # One of them is not labeled yet.
                    dp[y] = dp[x] = max(p1, p2)
                elif (p1 != p2):
                    # merge two provinces
                    provIdx += 1
                    provinces[provIdx] = provIdx
                    provinces[p1] = provIdx
                    provinces[p2] = provIdx
        result = 0
        for i in range(1, provIdx + 1):
            if provinces[i] == i:
                result += 1
        return result
