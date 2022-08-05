from typing import List
from sys import path
path.append("../utils")
from measure import measure

class Solution:
    def myPow(self, x: float, y: int) -> float:
        """
        Pythonユーザーはここにコードを書いてください
        """

        if (y == 0):
            return -1 if x < 0 else 1

        isNegative = False
        if (y < 0):
            isNegative = True
            y = -y

        result = 1
        while(y > 0):
            if (y & 1):
                result *= x
            x = x * x
            y = y >> 1


        return 1 / result if isNegative else result


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

    results.append(test("test1", func, 3, 3, 27))
    results.append(test("test2", func, 3, 8, 6561))
    results.append(test("test3", func, 2.0, -2, 0.25))
    results.append(test("test4", func, 1.0000004, 10000000, 54.59811))
    results.append(test("test5", func, 1.0000000004, 214783647, 1.08971))
    results.append(test("test6", func, 1.0000000004, -214783648, 0.91767))
    results.append(test("test7", func, 1.0000000004, -214783648, 0.91767))
    results.append(test("test8", func, 0, 0, 1))
    results.append(test("test9", func, -13.62608, 3, -2529.95504))
    results.append(test("test10", func, 2, -214748364, 0))

    total = 0
    for result in results:
        total += result[0]
        print(result)
    print("total = {} msec".format(total / 1000))


if __name__ == "__main__":
    instance = Solution()
    runTests(instance.myPow)
