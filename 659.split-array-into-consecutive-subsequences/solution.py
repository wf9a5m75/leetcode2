class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        size = len(nums)
        if size < 3:
            return False

        lastNum = nums[size - 1]
        patterns = [ [lastNum, 1] ]

        for i in range(size - 2, -1, -1):
            expectNum = nums[i] + 1
            L = 0
            R = len(patterns) - 1
            while(L < R):
                mid = (L + R) >> 1
                if (patterns[mid][0] == expectNum):
                    R = mid
                elif (patterns[mid][0] < expectNum):
                    L = mid + 1
                else:
                    R = mid - 1
            if (patterns[R][0] == expectNum):
                patterns[R][0] = nums[i]
                patterns[R][1] += 1
            else:
                patterns.insert(0, [nums[i], 1])


        for pattern in patterns:
            if pattern[1] < 3:
                return False
        return True
