class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        mask = 10**(k - 1)
        rest = num

        # num = 1234567
        # B = 567
        # rest = 1234
        nextRest = rest // 10**k
        B = rest - (nextRest * 10**k)
        rest = nextRest
        cnt = 1 if (B > 0) and (num % B == 0) else 0


        while rest > 0:
            # B = 56
            # nextRest = 123
            B = B // 10
            nextRest = rest // 10

            # B = 56 + (1234 - 1230) * 100 = 456
            B = B + (rest - nextRest * 10) * mask
            cnt = cnt + (1 if (B > 0) and (num % B == 0) else 0)
            rest = nextRest
        return cnt
