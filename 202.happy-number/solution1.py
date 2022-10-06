class Solution:
    def isHappy(self, n: int) -> bool:
        faster = slower = n
        while(faster != 1):
            faster = self.getNext(self.getNext(faster))
            slower = self.getNext(slower)
            if faster == slower:
                return faster == 1
        return True

    @cache
    def getNext(self, n: int) -> int:
        result = 0
        while(n > 0):
            result += (n % 10) ** 2
            n //= 10
        return result
