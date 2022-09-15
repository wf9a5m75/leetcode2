class Solution:
    def search(self, nums: List[int], target: int) -> bool:


        def binarySearch(L: int, R: int) -> bool:
            if (L > R):
                return False
            mid = (L + R) >> 1

            if (nums[mid] == target):
                return True
            if (nums[L] == nums[mid]) and (nums[R] == nums[mid]):
                # we don't know where the lowest value is.
                # find in both.
                return (binarySearch(L, mid - 1) or binarySearch(mid + 1, R))

            elif ((nums[L] <= target < nums[mid]) or
                  ((nums[L] > nums[mid]) and (target < nums[mid])) or
                  ((nums[L] > nums[mid]) and (nums[L] <= target))):

                return binarySearch(L, mid - 1)
            else:
                return binarySearch(mid + 1, R)

        return binarySearch(0, len(nums) - 1)
