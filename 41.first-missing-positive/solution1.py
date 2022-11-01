class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.append(0)
        size = len(nums)
        cnt = 0

        # Cycle sorting (O(N*N))
        while(cnt < size - 1):
            if (nums[cnt] == cnt) or (nums[cnt] < 0) or (nums[cnt] >= size):
                cnt += 1
                continue

            i = cnt
            j = nums[cnt]
            nums[i], nums[j] = nums[j], nums[i]

            if (nums[cnt] == cnt) or (nums[i] == nums[j]):
                cnt += 1

        for i in range(1, size):
            if (nums[i] != i):
                return i
        return size
