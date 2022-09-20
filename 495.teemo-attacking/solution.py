class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        lastT = timeSeries.pop(0)
        nextT = lastT + duration
        result = 0

        size = len(timeSeries)
        i = 0
        while(i < size):
            if (timeSeries[i] <= nextT):
                result += timeSeries[i] - lastT
            else:
                result += duration
            nextT = timeSeries[i] + duration
            lastT = timeSeries[i]
            i += 1
        result += duration

        return result
