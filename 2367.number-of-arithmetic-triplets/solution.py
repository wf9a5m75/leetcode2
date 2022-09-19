class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        lookup = [-1] * 201
        for i, num in enumerate(nums):
            lookup[num] = i

        result = 0
        for numI in nums:
            numJ = numI + diff
            numK = numJ + diff

            if ((numJ <= 200) and (numK <= 200) and
                (lookup[numJ] >= 0) and (lookup[numK] >= 0)):
                result += 1
        return result
