#
# Time complexity: O(R)  ... R = n * O(1)
# Space complexity: O(1)
#
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if (n == 1):
            return 0

        prevK = ceil(k / 2)
        result = self.kthGrammar(n - 1, prevK)

        resultBits = [0, 1] if result == 0 else [1, 0]


        if (k & 1 == 1):
            return resultBits[0]
        else:
            return resultBits[1]
