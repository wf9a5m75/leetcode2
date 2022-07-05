class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        results = []
        nums.sort()
        size = len(nums)
        prevA = -1000001
        for aIdx in range(0, size - 2):
            A = nums[aIdx]
            if (A == prevA):
                continue

            prevA = A

            bIdx = aIdx + 1
            cIdx = size - 1
            while(bIdx < cIdx):
                B = nums[bIdx]
                C = nums[cIdx]
                s = A +B + C
                if (s == 0):
                    results.append([A, B, C])

                if s < 0:
                    while(bIdx < cIdx) and (nums[bIdx] == B):
                        bIdx += 1
                else:
                    while(bIdx < cIdx) and (nums[cIdx] == C):
                        cIdx -= 1
        return results
