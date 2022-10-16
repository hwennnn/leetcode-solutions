class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.arr = [None] * n
        self.n = n

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1
        self.arr[id] = value
        res = []
        for i in range(self.ptr, self.n):
            if self.arr[i] != None:
                res.append(self.arr[i])
            else:
                self.ptr = i
                break
        
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)