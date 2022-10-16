class SmallestInfiniteSet:

    def __init__(self):
        self.A = [True] * (1001)
        self.index = 1

    def popSmallest(self) -> int:
        res = 0
        
        for i in range(1, len(self.A)):
            if self.A[i]:
                res = i
                self.A[i] = False
                break
        
        return res

    def addBack(self, num: int) -> None:
        self.A[num] = True


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)