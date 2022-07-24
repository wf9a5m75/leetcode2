class MinStack:

    def __init__(self):
        self.valueStack = []
        self.minStack = []
        self.size = 0

    def push(self, val: int) -> None:
        if (self.size == 0) or (self.minStack[-1] >= val):
            self.minStack.append(val)

        self.valueStack.append(val)
        self.size += 1

    def pop(self) -> None:
        val = self.valueStack.pop()
        if (len(self.minStack) > 0) and (self.minStack[-1] == val):
            self.minStack.pop()
        self.size -= 1

    def top(self) -> int:
        return self.valueStack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
