class Solution:
    def intToRoman(self, num: int) -> str:
        romanNums = [
            [1, "I"], [4, "IV"], [5, "V"], [9, "IX"],
            [10, "X"], [40, "XL"], [50, "L"], [90, "XC"],
            [100, "C"], [400, "CD"], [500, "D"], [900, "CM"],
            [1000, "M"]
        ]

        result = ""
        R = len(romanNums) - 1
        while(rest > 0):

            if (num < romanNums[R][0]):
                # Subtract using binary search
                # Since the num value is smaller than before, we can use the "previous R" as R
                L = 0
                while(L <= R):
                    mid = (L + R) >> 1
                    if (romanNums[mid][0] > num):
                        R = mid - 1
                    else:
                        L = mid + 1

            result += romanNums[R][1]
            num -= romanNums[R][0]
        return result
