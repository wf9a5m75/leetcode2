#
# Python / TLE
#
# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         factor = 1
#         result = 0
#         MOD = 1000000007
#         for i in range(n, 0, -1):
#             while(i > 0):
#                 result = (result + ((i & 1) * factor)) % MOD
#                 i >>= 1
#                 factor = (factor * 2) % MOD
#         return result
#
# print("result = ", Solution().concatenatedBinary(50995))

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        bin_len = 0
        ans = 0
        MOD = 1000000007
        for i in range(1, n + 1):
            if ((i & (i - 1)) == 0):
                bin_len += 1
            ans = ((ans << bin_len) % MOD + i) % MOD
        return ans
