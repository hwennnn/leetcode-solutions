class ProductOfNumbers:
    
    def __init__(self):
        self.A = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.A = [1]
        else:
            self.A.append(self.A[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.A)
        if k >= n : return 0
        
        return self.A[-1] // self.A[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)