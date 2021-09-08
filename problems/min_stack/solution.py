class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mmin = float('inf')

    def push(self, val: int) -> None:
        self.mmin = min(self.mmin, val)
        self.stack.append((val, self.mmin))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.mmin = self.stack[-1][1]
        else:
            self.mmin = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()