class MinStack:

    def __init__(self):
        self.stack = []        
        self.mmin = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.mmin[-1]:
            self.mmin.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.mmin[-1] == popped:
            self.mmin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mmin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()