class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        hq = []
        for num in counts.keys():
            if (len(hq) < k):
                heapq.heappush(hq, (counts[num], num))
            else:
                heapq.heappushpop(hq, (counts[num], num))
        results = []
        for item in hq:
            results.append(item[1])
        return results
