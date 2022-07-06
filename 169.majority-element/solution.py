class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityNums = [nums[0], 2**31]
        counters = [0, 0]

        #
        # voting
        #
        for num in nums:
            if num == majorityNums[0]:
                counters[0] += 1
            elif num == majorityNums[1]:
                counters[1] += 1
            else:

                if counters[0] == 0:
                    majorityNums[0] = num
                    counters[0] = 1
                elif counters[1] == 1:
                    majorityNums[1] = num
                    counter[1] = 1
                else:
                    counters[0] -= 1
                    counters[1] -= 1

        #
        # majorityNums[0] or majorityNums[1] should be the majority number.
        # Double check them
        #
        counters = [0, 0]
        for num in nums:
            counters[0] += 1 if majorityNums[0] == num else 0
            counters[1] += 1 if majorityNums[1] == num else 0

        threthold = len(nums) / 2
        if (counters[0] >= threthold):
            return majorityNums[0]
        elif (counters[1] >= threthold):
            return majorityNums[1]
        else:
            return -1
