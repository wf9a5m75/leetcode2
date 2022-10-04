class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        size = len(colors)
        result = 0
        i = 0
        while(i < size):

            largestTime = timeSum = neededTime[i]
            j = i + 1
            while(j < size) and (colors[i] == colors[j]):
                largestTime = max(largestTime, neededTime[j])
                timeSum += neededTime[j]
                j += 1
            timeSum -= largestTime
            result += timeSum

            i = j
        return result
            
