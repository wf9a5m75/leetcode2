class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        diff = right - left

        mask = 1
        while(diff > 0):
            left >>= 1
            right >>= 1
            diff >>= 1
            mask <<= 1
        while(left > 0) and (right > 0):
            if (left & 1) == 1 and (right & 1) == 1:
                result |= mask
            mask <<= 1
            left >>= 1
            right >>= 1
        return result
