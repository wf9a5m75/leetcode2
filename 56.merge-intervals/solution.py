class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        intervals.sort(key = lambda timeSpan: timeSpan[0])

        N = len(intervals)
        results = [intervals[0]]
        for i in range(1, N):
            if (intervals[i][0] > results[-1][1]):
                results.append(intervals[i])
            else:
                results[-1][1] = max(results[-1][1], intervals[i][1])
        return results
