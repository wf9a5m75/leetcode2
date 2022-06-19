from typing import List
import sys
sys.path.append("../utils")
from measure import measure

#
# Time complexity: O(N)
# Space complexity: O(1)
#
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)


        minimum = -2 ** 31
        max3 = [ None, None, None ]

        for num in nums:
            if (num == max3[0]) or (num == max3[1]):
                continue

            if (max3[0] is None) or (num > max3[0]):
                max3[2], max3[1] = max3[1], max3[0]
                max3[0] = num

            elif (max3[1] is None) or (num > max3[1]):
                max3[2] = max3[1]
                max3[1] = num

            elif (max3[2] is None) or (num >= max3[2]):
                max3[2] = num

        if (max3[2] is not None):
            return max3[2]
        else:
            return max3[0]



def test(caseName, func, nums, expectResult):
    result = measure(func)(nums)

    testResult = "pass" if result[1] == expectResult else "fail"
    return [result[0], caseName, testResult]


def checkTests(func):
    results = []

    results.append(test("test1", func, [2,2,3,1], 1))
    results.append(test("test2", func, [1,2], 2))
    results.append(test("test3", func, [3,2,1], 1))
    results.append(test("test4", func, [1,2,3], 1))
    results.append(test("test5", func, [0,0,1], 1))
    results.append(test("test6", func, [2,2,1,1,1,3,3,3,1,2,3,4,5,1,12], 4))
    results.append(test("test7", func, [1,2,3], 1))
    results.append(test("test8", func, [-2147483648, -2147483647, -2147483647], -2147483647))
    results.append(test("test9", func, [1,1,2], 2))
    results.append(test("test10", func, [1,-2147483648,2], -2147483648))

    total = 0
    for result in results:
        total += result[0]
        print(result)
    print("total = {} msec".format(total / 1000))


if __name__ == "__main__":
    instance = Solution()
    checkTests(instance.thirdMax)
