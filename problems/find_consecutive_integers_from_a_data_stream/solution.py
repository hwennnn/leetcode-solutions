class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.A = deque()

    def consec(self, num: int) -> bool:        
        if num == self.value:
            self.A.append(num)
        else:
            self.A.clear()
            
        if len(self.A) > self.k:
            self.A.popleft()
        
        return len(self.A) == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)