class LazySegmentTree:
    def __init__(self, low, high, val):
        self.low = low
        self.high = high
        self.val = val
        self.lazy = 0
        self.left = None
        self.right = None
    
    def _extend(self):
        if self.low < self.high:
            if self.left is None:
                mid = (self.low + self.high) // 2
                self.left = LazySegmentTree(self.low, mid, self.val)
                if mid + 1 <= self.high:
                    self.right = LazySegmentTree(mid + 1, self.high, self.val)
            elif self.lazy != 0:
                self.left.val += self.lazy
                self.left.lazy += self.lazy
                self.right.val += self.lazy
                self.right.lazy += self.lazy
        self.lazy = 0
        
    def update(self, low, high, delta):
        if low > high or self.high < low or high < self.low:
            return
        if low <= self.low and self.high <= high:
            self.val += delta
            self.lazy += delta
            return
        self._extend()
        self.left.update(low, high, delta)
        self.right.update(low, high, delta)
        self.val = max(self.left.val, self.right.val)
    
    def query(self, low, high):
        if low > high or self.high < low or high < self.low:
            return 0
        if low <= self.low and self.high <= high:
            return self.val
        self._extend()
        return max(self.left.query(low, high), self.right.query(low, high))

class MyCalendarThree:

    def __init__(self):
        self.st = LazySegmentTree(0, 10 ** 9, 0)

    def book(self, start: int, end: int) -> int:
        self.st.update(start, end - 1, 1)
        
        return self.st.query(0, 10 ** 9)


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)