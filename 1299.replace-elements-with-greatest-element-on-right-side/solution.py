class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largestR = -1
        size = len(arr)
        for i in range(size - 1, -1, -1):
            val = arr[i]
            arr[i] = largestR
            largestR = max(largestR, val)
        return arr
