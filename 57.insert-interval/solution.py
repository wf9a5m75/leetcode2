class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals)

        # find the insert position using binary search
        L = 0
        R = size - 1
        while(L <= R):
            mid = (L + R) >> 1
            if (intervals[mid][0] <= newInterval[0]):
                L = mid + 1
            else:
                R = mid - 1

        # insert the new interval
        if (L == size):
            intervals.append(newInterval)
        else:
            intervals.insert(L, newInterval)
        i = max(R, 0)
        size += 1

        # if necessary, merge intervals
        while(i + 1 < size):
            while(i + 1 < size) and (intervals[i][1] >= intervals[i + 1][0]):
                other = intervals.pop(i + 1)
                intervals[i][0] = min(intervals[i][0], other[0])
                intervals[i][1] = max(intervals[i][1], other[1])
                size -= 1
            i += 1

        return intervals
