#
# DP approach
#  time complexity: O(N)
#  space complexity: O(N)
#
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        size = len(nums)
        largest = [size - 1] * size
        smallest = [0] * size

        k = size - 2
        for i in range(1, size):
            if nums[smallest[i - 1]] > nums[i]:
                smallest[i] = i
            else:
                smallest[i] = smallest[i - 1]

            if nums[largest[k + 1]] < nums[k]:
                largest[k] = k
            else:
                largest[k] = largest[k + 1]
            k -= 1
        # print(smallest)
        # print(largest)

        for i in range(1, size - 1):
            a = smallest[i]
            b = i
            c = largest[i]

            if (a < b < c) and (nums[a] < nums[b] < nums[c]):
                return True
        return False
