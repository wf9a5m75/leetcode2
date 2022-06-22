class Solution:
    def isHappy(self, n: int) -> bool:
        appears = set()
        s = 0
        while(s != 1):
            s = 0
            while(n > 0):
                d = n % 10
                s += d * d
                n = n // 10
            if (s in appears):
                return False
            appears.add(s)
            n = s
        return True
