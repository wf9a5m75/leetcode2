class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negatives = []
        zeros = []
        positives = []
        results = set()

        nums.sort()

        for num in nums:
            if num == 0:
                zeros.append(num)
            elif num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)

        # The case: 0, 0, 0
        if (len(zeros) >= 3):
            results.add((0,0,0))

        pSet = set(positives)
        nSet = set(negatives)

        # The case:  3 - 3 + 0
        if (len(zeros) > 0):
            for num in pSet:
                if -num in nSet:
                    results.add((num, -num, 0))

        # The case: 3 + 3 - 6
        pSize = len(positives)
        for i in range(pSize - 1):
            for j in range(i + 1, pSize):
                rest = -(positives[i] + positives[j])
                if (rest in nSet):
                    results.add((positives[i], positives[j], rest))

        # The case: -3 -3 + 6
        nSize = len(negatives)
        for i in range(nSize - 1):
            for j in range(i + 1, nSize):
                rest = -(negatives[i] + negatives[j])
                if (rest in pSet):
                    results.add((negatives[i], negatives[j], rest))

        return results
            
