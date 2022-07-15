class Solution:
    def numberOfSteps(self, num: int) -> int:
        if (num == 0):
            return 0
        if (num % 2 == 1):
            return self.numberOfSteps(num - 1) + 1
        else:
            return self.numberOfSteps(num / 2) + 1
