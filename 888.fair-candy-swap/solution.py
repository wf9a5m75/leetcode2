class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        bobSet = set(bobSizes)

        even = (bobSum - aliceSum) >> 1

        for aBox in aliceSizes:
            if (even + aBox) in bobSet:
                return [aBox, even + aBox]
