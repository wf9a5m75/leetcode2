class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        intervals.sort(key = lambda x: x[0])

        # pick the first interval
        results = [intervals.pop(0)]

        for period in intervals:
            if results[-1][1] < period[0]:
                # not overlap
                results.append(period)
            else:
                # overlap
                results[-1][0] = min(period[0], results[-1][0])
                results[-1][1] = max(period[1], results[-1][1])
        return results
