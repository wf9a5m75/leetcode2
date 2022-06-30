from typing import List
from sys import path
path.append("../utils")
from measure import measure


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (x == 0):
            return 1 if n == 0 else 0
        if (x == -1):
            return 1 if (n % 2 == 0) else -1

        absX = abs(x)
        mem = {
            0: 1,
            1: absX,
            2: absX * absX
        }
        def helper(x, n):
            orgN = n
            # print("x = {}, n = {}".format(x, n))

            if (n in mem):
                return mem[n]

            cnt = 0
            isOddN = n & 1 == 1
            if (isOddN):
                n -= 1

            while(n & 1 == 0):
                n = n >> 1
                cnt += 1

            tmp = helper(x, n)
            for _ in range(cnt):
                tmp *= tmp

            if (isOddN):
                tmp *= x

            # print("  ({}) return {}".format(orgN, tmp))
            mem[n] = tmp
            return tmp


        result = helper(x, abs(n))

        if n < 0:
            return 1 / result
        else:
            return result

# -------------------------------------------------------------
# Following statements are for test.
#
#  $> python3 solution.py
# -------------------------------------------------------------
def test(caseName, func, x, n, expectResult):
    result = measure(func)(x, n)
    result[1] = round(result[1], 5)
    if result[1] != expectResult:
        print("   yout answer: ", result[1])
        print("   expectation: ", expectResult)

    testResult = "pass" if result[1] == expectResult else "fail"
    return [result[0], caseName, testResult]

def runTests(func):
    results = []

    # results.append(test("test1", func, 3, 3, 27))
    results.append(test("test2", func, 3, 8, 6561))
    results.append(test("test2", func, 2.0, -2, 0.25))
    results.append(test("test3", func, 1.0000004, 10000000, 54.59811))
    results.append(test("test4", func, 1.0000000004, 214783647, 1.08971))
    results.append(test("test4", func, 1.0000000004, -214783648, 0.91767))
    results.append(test("test4", func, 1.0000000004, -214783648, 0.91767))
    results.append(test("test4", func, 0, 0, 1))
    results.append(test("test4", func, -13.62608, 3, -2529.95504))

    total = 0
    for result in results:
        total += result[0]
        print(result)
    print("total = {} msec".format(total / 1000))


if __name__ == "__main__":
    instance = Solution()
    runTests(instance.myPow)
