class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        size = len(arr)
        if (size < 3):
            return False

        peakL = 0
        peakR = size - 1
        prev = arr[0] - 1
        while((peakL < size) and (prev < arr[peakL])):
            prev = arr[peakL]
            peakL += 1

        prev = arr[peakR] - 1
        while((peakR >= 0) and (arr[peakR] > prev)):
            prev = arr[peakR]
            peakR -= 1
        # print("peakL={0}, peakR={1}, size={2}".format(peakL - 1, peakR + 1, size))
        return (peakL - 1 == peakR + 1) and (peakR + 1 < size - 1) and (peakL - 1 > 0)
