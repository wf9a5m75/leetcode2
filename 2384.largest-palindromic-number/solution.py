class Solution:
    def largestPalindromic(self, num: str) -> str:
        counts = [0] * 10

        kinds = 0
        for c in num:
            idx = int(c)
            counts[idx] += 1
            kinds |= 1 << idx

        result = ""
        for i in range(9, -1, -1):
            if (counts[i] & 1) == 1:
                if result == "":
                    result = str(i)
                counts[i] -= 1
                if counts[i] == 0:
                    kinds = kinds ^ (1 << i)

        if (kinds != 1):
            for i in range(10):
                cnt = counts[i] >> 1
                if cnt > 0:
                    c = str(i)
                    result = f"{c * cnt}{result}{c * cnt}"
                    counts[i] = 0

        result = "0" if result == "" else result
        return result
