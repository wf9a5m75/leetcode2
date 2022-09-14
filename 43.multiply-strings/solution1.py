"""
                   1      2        3
                 x 4      5        6
                -----------------------
                 (1*6)    (2*6)    (3*6)
        (1*5)    (2*5)    (3*5)
 (1*4)  (2*4)    (3*4)
------------------------------------------
4     5+8      6+10+12   12+15    18
  ←1←     ←3←         ←2←    ← 1 ←
5        6          0       8       8
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (num1 == "0") or (num2 == "0"):
            return "0"

        size1 = len(num1)
        size2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]

        dp = [0] * (size1 + size2)
        for i in range(size2):
            d2 = int(num2[i])

            for j in range(size1):
                d1 = int(num1[j])
                tmp = dp[i + j] + (d2 * d1)

                dp[i + j] = tmp % 10
                dp[i + j + 1] += tmp // 10
        if (dp[-1] == 0):
            dp.pop()

        result = ""
        while(dp):
            result = result + str(dp.pop())

        return result
            
