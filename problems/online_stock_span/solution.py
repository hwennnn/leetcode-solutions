class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        curr = 1
        
        while self.stack and self.stack[-1][0] <= price:
            prior, streak = self.stack.pop()
            curr += streak
        self.stack.append((price, curr))
        return curr

    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)