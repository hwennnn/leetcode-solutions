class MinStack:

    def __init__(self):
        self.stack = []
        self.m = float('inf')
        
    def push(self, x: int) -> None:
        self.m = min(self.m, x)
        self.stack.append((x, self.m))

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) > 0:
            self.m = self.stack[-1][1]
        else:
            self.m = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()