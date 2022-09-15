from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        plates = {}
        candles = []

        def binarySearch(idx: int) -> List[int]:
            L = 0
            R = len(candles) - 1
            while(L <= R):
                mid = (L + R) >> 1
                if (candles[mid] == idx):
                    return [mid, mid]
                elif (candles[mid] < idx):
                    L = mid + 1
                else:
                    R = mid - 1
            return [R, L]

        hasCandle = False
        cnt = 0
        for i, char in enumerate(s):
            if (char == "|"):
                candles.append(i)
                plates[i] = cnt
                hasCandle = True
            elif (hasCandle):
                cnt += 1

        # print('candles', candles)
        # print('plates', plates)
        results = []
        for start, end in queries:
            _, L = binarySearch(start)
            if (L == len(candles)):
                results.append(0)
                continue
            R, _ = binarySearch(end)
            if (R == -1) or (L >= R):
                results.append(0)
                continue

            #print(f"L={L}, R={R}")
            # print(f"candles[L]={candles[L]},candles[R]={candles[R]}")

            cnt = plates[candles[R]] - plates[candles[L]]
            # cnt = 0
            # for i in range(L + 1, R + 1):
            #     cnt += plates[candles[i]]

            results.append(cnt)
        return results

            

f = open("./test.txt", "r")
lines = f.readlines()
f.close()


print(Solution().platesBetweenCandles(eval(lines[0]), [[2,99923]]))
