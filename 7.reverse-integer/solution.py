class Solution:
    def createIntFromArray(self, nums: List[int], hasMinus: bool)-> int:
        y = 0
        for d in nums:
            y = y * 10 + d
        if (hasMinus):
            y *= -1
        return y

    def reverse(self, x: int) -> int:
        if (x == 0):
            return 0
        hasMinus = (x < 0)
        x = abs(x)

        buffer = []
        while(x > 0):
            d = x % 10
            buffer.append(d)
            x //= 10

        if (len(buffer) < 10):
            return self.createIntFromArray(buffer, hasMinus)

        if (len(buffer) > 10):
            return 0

        limit = [2,1,4,7,4,8,3,6,4,7]
        if (hasMinus):
            limit[-1] += 1

        for i in range(10):
            if (buffer[i] < limit[i]):
                break

            if (limit[i] < buffer[i]):
                return 0

        return self.createIntFromArray(buffer, hasMinus)
