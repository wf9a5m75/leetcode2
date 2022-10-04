class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        size = len(colors)
        @cache
        def backtrack(i: int, prevIdx: int) -> int:
            if (i >= size):
                return 0

            if colors[prevIdx] != colors[i]:
                return backtrack(i + 1, i)

            h = [-neededTime[prevIdx]]
            while(i < size) and (colors[prevIdx] == colors[i]):
                heapq.heappush(h, -neededTime[i])
                i += 1
            heapq.heappop(h)


            times = 0
            while(h):
                times -= heapq.heappop(h)
            return backtrack(i + 1, i) + times
        return backtrack(1, 0)
            
