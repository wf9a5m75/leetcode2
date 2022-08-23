class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack = []
        results = [0] * len(nums)
        for i, val in enumerate(nums):
            while(stack) and (nums[stack[-1]] < val):
                topIdx = stack.pop()
                results[topIdx] = i - topIdx
            stack.append(i)

        return results
