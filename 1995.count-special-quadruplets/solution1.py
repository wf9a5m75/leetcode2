class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        seenAlready = defaultdict(int)
        count = 0
        n = len(nums)
        for a in range(n-1,0,-1):
            for b in range(a-1,-1,-1):
                count += seenAlready[nums[a]+nums[b]]
            for d in range(n-1,a,-1):
                seenAlready[nums[d]-nums[a]] += 1
        return count
