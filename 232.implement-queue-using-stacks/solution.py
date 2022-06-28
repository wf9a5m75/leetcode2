class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.lastAction = "write"

    def push(self, x: int) -> None:

        if (self.lastAction != "write"):
            self._flipStacks(self.s2, self.s1)
        self.s1.append(x)
        self.lastAction = "write"


    def _flipStacks(self, src, dst):
        while(src):
            dst.append(src.pop())

    def pop(self) -> int:
        if (self.lastAction != "read"):
            self._flipStacks(self.s1, self.s2)
        self.lastAction = "read"
        return self.s2.pop()

    def peek(self) -> int:
        if (self.lastAction != "read"):
            self._flipStacks(self.s1, self.s2)
        self.lastAction = "read"
        return self.s2[-1]


    def empty(self) -> bool:
        return (len(self.s1) == 0) and (len(self.s2) == 0)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
