#
#   time complexity: O(N)
#   space complexity: O(1)
#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers) - 1
        while(idx1 < idx2):
            s = numbers[idx1] + numbers[idx2]
            if (s == target):
                return [idx1 + 1, idx2 + 1]
            elif (s < target):
                idx1 += 1
            else:
                idx2 -= 1
        return [-1, -1]
