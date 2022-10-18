class Solution:
    def countAndSay(self, n: int) -> str:

        prev = [1]
        for _ in range(n - 1):
            i = 0
            size = len(prev)
            result = []
            while(i < size):
                pVal = prev[i]
                L = i
                R = L + 1
                while(R < size) and (pVal == prev[R]):
                    R += 1
                result.append(R - L)
                result.append(pVal)
                i = R
            prev = result
        return "".join(map(lambda x :  str(x), prev))
