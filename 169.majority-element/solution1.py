class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mem = [[nums[0], 0], [None, 0]]
        for num in nums:
            if (mem[0][0] == num):
                mem[0][1] += 1

            elif (mem[1][0] == num):
                mem[1][1] += 1

            else:
                if mem[0][1] <= 0:
                    mem[0][0] = num
                    mem[0][1] = 1

                elif mem[1][1] <= 0:
                    mem[1][0] = num
                    mem[1][1] = 1
                else:
                    mem[0][1] -= 1
                    mem[1][1] -= 1


        mem[0][1] = 0
        mem[1][1] = 0
        for num in nums:
            for i in range(2):
                if (num == mem[i][0]):
                    mem[i][1] += 1
                    break

        half = len(nums) / 2
        if (mem[0][1] >= half):
            return mem[0][0]
        else:
            return mem[1][0]
