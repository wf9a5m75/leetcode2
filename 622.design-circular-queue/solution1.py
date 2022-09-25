class MyCircularQueue:

    def __init__(self, k: int):
        self.buffer = [0] * k
        self.limit = k
        self.start = 0
        self.cnt = 0

    def enQueue(self, value: int) -> bool:
        if (self.isFull()):
            return False
        self.buffer[(self.start + self.cnt) % self.limit] = value
        self.cnt += 1
        return True


    def deQueue(self) -> bool:
        if (self.isEmpty()):
            return False

        self.start = (self.start + 1) % self.limit
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.buffer[self.start]


    def Rear(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.buffer[(self.start + self.cnt - 1) % self.limit]


    def isEmpty(self) -> bool:
        return self.cnt == 0


    def isFull(self) -> bool:
        return self.cnt == self.limit



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
