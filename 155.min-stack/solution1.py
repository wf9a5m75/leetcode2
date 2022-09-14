class MinStack:

    def __init__(self):
        self.minValues = [float('inf')]
        self.values = [float('inf')]

    def push(self, val: int) -> None:
        if (self.minValues[-1] >= val):
            self.minValues.append(val)
        self.values.append(val)

    def pop(self) -> None:
        val = self.values.pop()
        if (self.minValues[-1] == val):
            self.minValues.pop()

    def top(self) -> int:
        return self.values[-1]


    def getMin(self) -> int:
        return self.minValues[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
