class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = self.tail = None
        self.len = 0
        self.limit = k

    def enQueue(self, value: int) -> bool:
        if (self.isFull()):
            return False

        if (self.head is None):
            self.tail = self.head = ListNode(value)
            self.len += 1
            return True

        self.tail.next = ListNode(value)
        self.tail = self.tail.next
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if (self.isEmpty()):
            return False

        self.head = self.head.next
        self.len -= 1
        return True

    def Front(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.head.value

    def Rear(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.tail.value


    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.limit



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
