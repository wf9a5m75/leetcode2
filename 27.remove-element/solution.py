class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            while(num >= 100):
                num = num / 100
            cnt += 1 if num >= 10 else 0
        return cnt
