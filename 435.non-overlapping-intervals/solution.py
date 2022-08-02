class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def compPeriod(a: List[int], b: List[int]) -> int:
            return a[1] - b[1]

        intervals.sort(key=cmp_to_key(compPeriod))

        last = intervals[0]
        validCnt = 1
        for i in range(1, len(intervals)):

            if (intervals[i][0] >= last[1]):
                validCnt += 1
                last = intervals[i]
        return len(intervals) - validCnt
