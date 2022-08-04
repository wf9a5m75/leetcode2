# https://leetcode.com/problems/mirror-reflection/discuss/2376355/Python3-oror-4-lines-geometry-w-explanation-oror-TM%3A-9281

class Solution:
    def gcd(self, a: int, b: int) -> int:
        if (a < b):
            b, a = a, b

        r = a % b
        while(r != 0):
            a = b
            b = r
            r = a % b
        return b

    def lcm(self, a: int, b: int) -> int:
        return (a * b) / self.gcd(a, b)


    def mirrorReflection(self, p: int, q: int) -> int:
        L = self.lcm(p, q)

        if (L // q) % 2 == 0:
            return 2
        return int((L // p) % 2)
