class Solution:
    def numberToWords(self, num: int) -> str:
        if (num == 0):
            return "Zero"
        numEng100 = [
            [1, "One"], [2, "Two"], [3, "Three"], [4, "Four"], [5, "Five"],
            [6, "Six"], [7, "Seven"], [8, "Eight"], [9, "Nine"], [10, "Ten"],
            [11, "Eleven"], [12, "Twelve"], [13, "Thirteen"], [14, "Fourteen"], [15, "Fifteen"],
            [16, "Sixteen"], [17, "Seventeen"], [18, "Eighteen"], [19, "Nineteen"], [20, "Twenty"],
            [30, "Thirty"], [40, "Forty"], [50, "Fifty"], [60, "Sixty"], [70, "Seventy"],
            [80, "Eighty"], [90, "Ninety"]
        ]

        result = []
        R = len(numEng100) - 1
        while(num > 0):
            if (num >= 100):
                scale = self.findScale(num)
                cnt = num // scale[0]
                if (cnt > 9):
                    result.append(self.numberToWords(cnt))
                else:
                    result.append(numEng100[cnt - 1][1]) # cnt = 1..9
                result.append(scale[1])

                num = num % scale[0]
            else:
                L = 0
                while(L <= R):
                    mid = (L + R) >> 1
                    if (numEng100[mid][0] <= num):
                        L = mid + 1
                    else:
                        R = mid - 1

                result.append(numEng100[R][1])

                num = num - numEng100[R][0]
        return " ".join(result)




    def findScale(self, num: int) -> List[Union[int, str]]:

        scaleRange = [
           [100, "Hundred"], [1000, "Thousand"], [1000000, "Million"],  [1000000000, "Billion"]
        ]
        if (num >= scaleRange[-1][0]):
            return scaleRange[-1]

        L = 0
        R = len(scaleRange) - 1
        while(L < R):
            mid = (L + R) >> 1
            if (scaleRange[mid][0] <= num) and (num < scaleRange[mid + 1][0]):
                return scaleRange[mid]
            elif (scaleRange[mid][0] < num):
                L = mid + 1
            else:
                R = mid - 1
        return scaleRange[L]

"""
# test codes
0
1
19
20
91
99
100
101
999
1000
1001
9999
10000
10001
99999
100000
100001
999999
1000000
1000001
9999999
10000000
10000001
99999999
100000000
100000001
999999999
1000000000
1000000001
2147483646
2147483647
"""
