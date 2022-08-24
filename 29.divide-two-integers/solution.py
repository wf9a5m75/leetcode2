class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2** 31 - 1
        INT_MIN = -2 ** 31

        if (dividend == 0 or divisor == 0):
            return 0
        elif (divisor == 1):
            return min(INT_MAX, max(INT_MIN, dividend))
        elif (divisor == -1):
            if dividend < 0:
                return min(INT_MAX, abs(dividend))
            else:
                return max(INT_MIN, -dividend)



        a = math.log(abs(dividend))
        b = math.log(abs(divisor))
        c = a - b
        result = int(math.exp(c) + 0.0000000001)
        if ((dividend < 0) and (divisor > 0) or
            (dividend > 0) and (divisor < 0)):
            result = -result

        return min(INT_MAX, max(INT_MIN, result))
