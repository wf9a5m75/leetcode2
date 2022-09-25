class MyCircularDeque:

    def __init__(self, k: int):
        self.buffer = [0] * k
        self.start = 0
        self.cnt = 0
        self.limit = k


    def insertFront(self, value: int) -> bool:
        if (self.isFull()):
            return False
        self.start = (self.start - 1) % self.limit
        self.buffer[self.start] = value
        self.cnt += 1
        return True

    def insertLast(self, value: int) -> bool:
        if (self.isFull()):
            return False
        i = (self.start + self.cnt) % self.limit
        self.buffer[i] = value
        self.cnt += 1
        return True


    def deleteFront(self) -> bool:
        if (self.isEmpty()):
            return False
        self.start = (self.start + 1) % self.limit
        self.cnt -= 1
        return True


    def deleteLast(self) -> bool:
        if (self.isEmpty()):
            return False
        self.cnt -= 1
        return True


    def getFront(self) -> int:
        if (self.isEmpty()):
            return -1

        return self.buffer[self.start]


    def getRear(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.buffer[(self.start + self.cnt - 1) % self.limit]

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.limit


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
