import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        N = len(points)

        # First k points are ok
        h = []
        for i in range(k):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            heapq.heappush(h, (-distance, points[i]))

        # After that, we need to pick the point if it is closer than the kth point.
        # Since Python heapq provides minimum-heapq,
        # we need to attach minus to store the item distance.
        #
        # For example, distance of points are h = [4,5,1,3,2]
        # If without minus, h[0] is 1.
        # But we want to pick up the point less than 5
        # That's why we need to flip the heapq sort as h = [-4, -5, -1, -3, -2]
        # Then h[0] becomses -5
        #
        for i in range(k, N):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            if (distance < -h[0][0]):
                heapq.heapreplace(h, (-distance, points[i]))

        # print(h)
        return list(map(lambda x: x[1], h))
