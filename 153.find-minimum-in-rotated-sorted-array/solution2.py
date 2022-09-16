class Solution:
    def findMin(self, nums: List[int]) -> int:

        L = 0
        R = len(nums) - 1
        while(L < R):
            mid = (L + R) >> 1
            if (nums[mid] > nums[R]):
                L = mid + 1
            elif (nums[L] < nums[mid]):
                R = mid - 1
            else:
                L += 1
                R -= 1
        return min(nums[L], nums[R])
