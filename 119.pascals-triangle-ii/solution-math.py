class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        factorial = [1]
        for i in range(rowIndex):
            factorial.append( factorial[i] * (i + 1) )

        def nCr(n : int, r: int) -> int:
            return int(factorial[n] / (factorial[r] * factorial[n - r]))


        results = [1] * (rowIndex + 1)
        L = 0
        R = rowIndex
        while(L <= R):
            results[R] = results[L] = nCr(rowIndex, R)
            L += 1
            R -= 1

        return results
