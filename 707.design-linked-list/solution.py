class ListNode:
    def __init__(self, next: Optional[ListNode], val: int):
        self.next = next
        self.val = val

class MyLinkedList:

    def __init__(self):
        # dummy head
        self.head = ListNode(None, -1)
        self.len = 0

    def get(self, index: int) -> int:
        if (index < 0) or (index >= self.len):
            return -1
        return self._moveTo(index).val


    def addAtHead(self, val: int) -> None:
        currHead = self.head.next
        newNode = ListNode(currHead, val)
        self.head.next = newNode
        self.len += 1


    def addAtTail(self, val: int) -> None:
        tail = self._moveTo(self.len - 1)
        tail.next = ListNode(None, val)
        self.len += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        if index == self.len:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return

        prev = self._moveTo(index - 1)
        currNext = prev.next
        newNode = ListNode(currNext, val)
        prev.next = newNode
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if (index < 0) or (index >= self.len):
            return
        if (index == 0):
            self.head.next = self.head.next.next
            self.len -= 1
            return
        prev = self._moveTo(index - 1)
        prev.next = prev.next.next
        self.len -= 1

    def _moveTo(self, index: int) -> ListNode:
        if (index < 0):
            return self.head
        head = self.head.next
        cnt = index // 2

        while(cnt > 0):
            head = head.next.next
            cnt -= 1
        if (index % 2 == 1):
            head = head.next
        return head




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
