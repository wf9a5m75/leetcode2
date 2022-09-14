class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.size = 0

    def get(self, index: int) -> int:
        if (index >= self.size) or (index < 0):
            return -1

        step2 = index >> 1
        p = self.head.next
        while(step2 > 0):
            p = p.next.next
            step2 -= 1
        if ((index & 1) == 1):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        p = ListNode(val)
        p.next = self.head.next
        self.head.next = p
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if (index > self.size):
            return

        step2 = index >> 1
        p = self.head
        while(step2 > 0):
            p = p.next.next
            step2 -= 1
        if ((index & 1) == 1):
            p = p.next
        pNext = p.next
        p.next = ListNode(val)
        p.next.next = pNext
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if (index < 0) or (index >= self.size):
            return

        step2 = index >> 1
        p = self.head
        while(step2 > 0):
            p = p.next.next
            step2 -= 1
        if ((index & 1) == 1):
            p = p.next
        p.next = p.next.next
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
