class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        last = intervals.pop(0)
        invalidCnt = 0
        for timespan in intervals:
            if timespan[0] >= last[1]:
                last = timespan
            else:
                invalidCnt += 1
        return invalidCnt
