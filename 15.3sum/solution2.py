class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        results = []

        prev = None
        for i, num in enumerate(nums):
            if prev == num:
                continue
            prev = num
            target = -1 * num
            j = i + 1
            k = size - 1
            while(j < k):
                s = nums[j] + nums[k]
                if (s < target):
                    curr = nums[j]
                    while(j < size) and (nums[j] == curr):
                        j += 1
                elif (s > target):
                    curr = nums[k]
                    while(k >= 0) and (nums[k] == curr):
                        k -= 1
                else:
                    results.append([nums[i], nums[j], nums[k]])

                    curr = nums[j]
                    while(j < size) and (nums[j] == curr):
                        j += 1

                    curr = nums[k]
                    while(k >= 0) and (nums[k] == curr):
                        k -= 1
        return results
