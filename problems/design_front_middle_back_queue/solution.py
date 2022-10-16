class FrontMiddleBackQueue:

    def __init__(self):
        self.A = collections.deque()
        self.B = collections.deque()
        
    def pushFront(self, val: int) -> None:
        self.A.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.A) > len(self.B):
            self.B.appendleft(self.A.pop())
        self.A.append(val)

    def pushBack(self, val: int) -> None:
        self.B.append(val)
        self.balance()

    def popFront(self) -> int:
        val = self.A.popleft() if self.A else -1
        self.balance()
        return val
        
    def popMiddle(self) -> int:
        val = self.A.pop() if self.A else -1
        self.balance()
        return val

    def popBack(self) -> int:
        val = self.B.pop() if self.B else self.A.pop() if self.A else -1
        self.balance()
        return val
        
    def balance(self) -> None:
        if len(self.A) > len(self.B) + 1:
            self.B.appendleft(self.A.pop())
        
        if len(self.A) < len(self.B):
            self.A.append(self.B.popleft())
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()