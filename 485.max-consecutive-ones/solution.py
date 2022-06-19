class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = cnt = 0 if nums[0] == 0 else 1
        i = 1
        while(i < len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                if maxOne < cnt:
                    maxOne = cnt
                cnt = 0
            i += 1
        maxOne = max(maxOne, cnt)
        return maxOne

            
