class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hq = []
        for row in matrix:
            for num in row:
                if (len(hq) < k):
                    heapq.heappush(hq, -num)
                else:
                    heapq.heappushpop(hq, -num)
        return -hq[0]
