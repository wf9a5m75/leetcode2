class Solution:
    def countOdds(self, low: int, high: int) -> int:
        cnt = 0
        if (low & 1 == 1):
            cnt += 1
            low += 1
        if (high & 1 == 1):
            cnt += 1
            high -= 1
        cnt += (high - low) >> 1
        return cnt
