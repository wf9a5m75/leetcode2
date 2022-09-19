class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = float('inf')

        i = 0
        while i < len(nums)-2:
            largest = nums[i] + nums[-1] + nums[-2]
            if largest < target:
                if abs(target - closest) > abs(target - largest):
                    closest = largest
                i += 1
                continue

            smallest =  nums[i] + nums[i+1] + nums[i+2]
            if smallest > target:
                if abs(target - closest) > abs(target - smallest):
                    closest = smallest
                break


            current_target = target - nums[i]

            while i > 0 and i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1

            j = i + 1
            k = len(nums) - 1

            while j < k:
                current_sum =nums[i] + nums[j] + nums[k]
                if abs(target - closest) > abs(target - current_sum):
                    closest = current_sum

                if nums[j] + nums[k] < current_target:
                    j += 1
                elif nums[j] + nums[k] > current_target:
                    k -= 1
                else:
                    return target

            i += 1

        return closest
