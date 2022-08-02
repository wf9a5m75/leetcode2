#
# Using heap
#  time complexity: O(k log N)
#  space complexity: O(k)
#
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        for num in nums:
            if (len(hq) < k):
                heapq.heappush(hq, num)
            else:
                heapq.heappushpop(hq, num)
        return hq[0]
