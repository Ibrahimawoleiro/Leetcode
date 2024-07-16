class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min.append(val)
        else:
            if self.min[-1] < val:
                self.stack.append(val)
                self.min.append(self.min[-1])
            else:
                self.stack.append(val)
                self.min.append(val)

    def pop(self) -> None:
        curr = self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()