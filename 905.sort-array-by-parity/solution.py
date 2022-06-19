#
# Two pointers approach
#  time compelixty: O(N)
#  space complexity: O(N)
#
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ptrEven = 0
        ptrOdd = size - 1
        while(ptrEven < ptrOdd):

            # should be even
            if (nums[ptrEven] & 1 == 0):
                ptrEven += 1

            # if not, find the even value from tail, and swap them
            else:
                while((ptrEven < ptrOdd) and (nums[ptrOdd] & 1 == 1)):
                    ptrOdd -= 1
                nums[ptrEven], nums[ptrOdd] = nums[ptrOdd], nums[ptrEven]
                ptrEven += 1
                ptrOdd -= 1
        return nums
