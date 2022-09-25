class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"{self.val} -> {self.next}"

class FrontMiddleBackQueue:

    def __init__(self):
        self.head = ListNode("(-1)")

    def pushFront(self, val: int) -> None:
        """
        (before) [-1] -> 3 -> None
        ------------------------
        (after) [-1] -> (new val) -> 3 -> None
        """
        headNext = self.head.next
        self.head.next = ListNode(val)
        self.head.next.next = headNext
        # print("pushFront", val, self.head)

    def pushMiddle(self, val: int) -> None:
        """
        (before) [-1] -> 3 -> 5 -> 6 -> 7 -> 4 -> None
                         f         f         f
                         s    s    s
        ------------------------
        (after) [-1] -> 3 -> 5 -> (new val) -> 6 -> 7 -> 4 -> None
        """
        fast = slow = self.head.next
        lastSlow = self.head

        while(fast and fast.next):
            fast = fast.next.next
            lastSlow = slow
            slow = slow.next

        slowNext = lastSlow.next
        lastSlow.next = ListNode(val)
        lastSlow.next.next = slowNext
        # print("pushMiddle", val, self.head)


    def pushBack(self, val: int) -> None:
        """
        (before) [-1] -> 3 -> 5 -> 6 -> 7 -> 4 -> None
                         p         p         p
        ------------------------
        (after) [-1] -> 3 -> 5 -> 6 -> 7 -> 4 -> (new val) -> None
        """
        p = self.head.next
        lastP = self.head

        while(p and p.next):
            lastP = p.next
            p = p.next.next

        if (p):
            lastP = p
        lastP.next = ListNode(val)
        # print("pushBack", val, self.head)

    def popFront(self) -> int:
        """
        (before) [-1] -> 3 -> 5 -> 6 -> 7 -> 4 -> None
        ------------------------
        (after) [-1] -> 5 -> 6 -> 7 -> 4 -> None
        """
        val = -1
        if (self.head.next):
            val = self.head.next.val
            headNextNext = self.head.next.next
            self.head.next = headNextNext

        # print("popFront", val, self.head)
        return val


    def popMiddle(self) -> int:
        if self.head.next is None:
            return -1
        fast = slow = self.head.next
        lastSlow = self.head
        lastSlow2 = self.head.next

        while(fast and fast.next):
            fast = fast.next.next
            lastSlow2 = lastSlow
            lastSlow = slow
            slow = slow.next

        if fast:
            """
            (before) [-1] -> 3 -> 5 -> 6 -> 7 -> 4 -> None
                             f         f         f
                             s    s    s
            ------------------------
            (after) [-1] -> 3 -> 5 -> 7 -> 4 -> None
            """
            slowNext = slow.next
            val = slow.val
            lastSlow.next = slowNext
        else:
            """
            (before) [-1] -> 3 -> 5 -> 6 -> 7 -> None
                             f         f
                             s    s
            ------------------------
            (after) [-1] -> 3 -> 6 -> 7 -> None
            """
            lastSlow2.next = lastSlow.next
            val = lastSlow.val
        # print("popMiddle", val, self.head)
        return val

    def popBack(self) -> int:
        """
        (before) [-1] -> 3 -> 5 -> 6 -> 7 -> 4 -> None
        ------------------------
        (after) [-1] -> 3 -> 5 -> 6 -> 7 -> None
        """
        if self.head.next is None:
            return -1
        p = self.head.next
        lastP = self.head

        while(p and p.next and p.next.next):
            lastP = p.next
            p = p.next.next

        if lastP.next and lastP.next.next:
            lastP = lastP.next

        val = lastP.next.val
        lastP.next = None
        # print("popBack", val, self.head)

        return val




# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
