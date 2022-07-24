import heapq

class SeatManager:

    def __init__(self, n: int):
        self.available = [i + 1 for i in range(n)]
        heapq.heapify(self.available)
        self.notAvailable = set()

    def reserve(self) -> int:
        seat = heapq.heappop(self.available)
        self.notAvailable.add(seat)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        self.notAvailable.remove(seatNumber)
        heapq.heappush(self.available, seatNumber)



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
