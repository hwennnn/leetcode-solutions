class RecentCounter:

    def __init__(self):
        self.s = []
        self.index = 0

    def ping(self, t: int) -> int:
        self.s.append(t)
        
        while self.index < len(self.s) and not (t - 3000 <= self.s[self.index] <= t):
            self.index += 1
        
        return len(self.s) - self.index
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)