class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n < 1):
            return False
        a = math.log10(n)
        b = math.log10(4)
        return (a / b).is_integer()
