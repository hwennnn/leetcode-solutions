class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if (len(self.arr) < self.size):
            self.arr.append(x)
            

    def pop(self) -> int:
        if len(self.arr) > 0:
            return self.arr.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i + 1 > len(self.arr):
                break
            
            self.arr[i] += val
                


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)