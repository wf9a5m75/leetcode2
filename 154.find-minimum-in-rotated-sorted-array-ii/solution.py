class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        if (size == 0):
            return float("inf")
        L = 0
        R = size - 1
        while(L + 1 < R):
            mid = (L + R) >> 1
            #print(L, mid, R)
            if (nums[mid] < nums[R]):
                R = mid
            elif (nums[mid] > nums[R]):
                L = mid
            else:
                if (nums[L] == nums[mid]) and (nums[mid] == nums[R]):
                    # test case for [10,1,10,10,10]

                    return min(self.findMin(nums[:mid]), self.findMin(nums[mid:]))
                if (nums[L] < nums[mid]):
                    R = mid
                else:
                    L = mid

        return min(nums[L], nums[R])
