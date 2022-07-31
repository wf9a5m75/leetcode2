class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        size = len(nums)
        rootN = sqrt(size)
        self.numOfBlocks = ceil(size / rootN)
        # print(f"self.numOfBlocks = {self.numOfBlocks}")

        self.blocks = [0] * self.numOfBlocks
        for i in range(size):
            self.blocks[i // self.numOfBlocks] += nums[i]

        # print(self.blocks)


    def update(self, index: int, val: int) -> None:
        blockIdx = index // self.numOfBlocks
        self.blocks[blockIdx] = self.blocks[blockIdx] - self.nums[index] + val
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        startBlockIdx = left // self.numOfBlocks
        endBlockIdx = right // self.numOfBlocks
        # print(f"start = {startBlockIdx}, end = {endBlockIdx}")

        result = 0
        if (startBlockIdx == endBlockIdx):
            for i in range(left, right + 1):
                result += self.nums[i]
        else:
            for i in range(left, (startBlockIdx + 1) * self.numOfBlocks):
                result += self.nums[i]
            # print(result)

            for i in range(startBlockIdx + 1, endBlockIdx):
                result += self.blocks[i]
            # print(result)

            for i in range(endBlockIdx * self.numOfBlocks, right + 1):
                result += self.nums[i]

            # print(endBlockIdx * self.numOfBlocks)
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
