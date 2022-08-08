from typing import List
from sys import path
path.append("../utils")
from measure import measure
import time

from functools import cache

class Solution:
    def myPow(self, x: float, y: int) -> float:

        # この問題が小数第5桁で丸めるので、それ以下は0
        if abs(x) < 0.00001:
            return 0

        # pow(x, 0) は常に 1
        if y == 0:
            return 1

        # y を正の整数に変えておく
        isNegative = y < 0
        y = abs(y)

        calcCache = [[1, x]]
        calcCacheIndicies = {1 : 0}

        @cache
        def getCache(target: int) -> int:
            # キャッシュが利用できる場合は利用する
            if (target in calcCacheIndicies):
                return calcCacheIndicies[target]

            # キャッシュがない場合は、一番近いキャッシュの値を使う
            L = 0
            R = len(calcCache) - 1
            while(L <= R):
                mid = (L + R) >> 1
                if (calcCache[mid][0] < target):
                    L = mid + 1
                else:
                    R = mid - 1

            return R

        result = 1
        result1 = x
        p = 1
        while ((p << 1) < y):
            p <<= 1
            if (p not in calcCacheIndicies):
                result1 *= result1
                calcCacheIndicies[p] = len(calcCache)
                calcCache.append([p, result1])
            else:
                result *= getCache(p)
                result1 = x
                y -= p
                p = 1

        result2 = 1
        y = y - p
        while(y > 0):
            cacheIdx = getCache(y)
            y -= calcCache[cacheIdx][0]
            result2 *= calcCache[cacheIdx][1]

        result = result * result1 * result2
        if isNegative:
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
    # results.append(test("test2", func, 3, 8, 6561))
    # results.append(test("test3", func, 2.0, -2, 0.25))
    # results.append(test("test4", func, 1.0000004, 10000000, 54.59811))
    # results.append(test("test5", func, 1.0000000004, 214783647, 1.08971))
    # results.append(test("test6", func, 1.0000000004, -214783648, 0.91767))
    # results.append(test("test7", func, 1.0000000004, -214783648, 0.91767))
    # results.append(test("test8", func, 2, -214748364, 0))
    # results.append(test("test9", func, -13.62608, 3, -2529.95504))
    results.append(test("test10", func, 2, -214748364, 0))
    # results.append(test("test11", func, 3, 7, 2187))

    total = 0
    for result in results:
        total += result[0]
        print(result)
    print("total = {} msec".format(total / 1000))


if __name__ == "__main__":
    instance = Solution()
    runTests(instance.myPow)
