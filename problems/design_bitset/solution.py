class Bitset:

    def __init__(self, size: int):
        self.n = size
        self.mask = [0] * size
        self.counts = 0
        self.hasFlip = False

    def fix(self, idx: int) -> None:
        if not self.hasFlip:
            self.fixHelper(idx)
        else:
            self.unfixHelper(idx)
        # print(self.toString())
    
    def fixHelper(self, idx):
        n = self.n - idx - 1
        
        if self.mask[idx] == 0:
            self.mask[idx] = 1
            self.counts += 1

    def unfix(self, idx: int) -> None:
        if self.hasFlip:
            self.fixHelper(idx)
        else:
            self.unfixHelper(idx)
    
    def unfixHelper(self, idx: int) -> None:
        n = self.n - idx - 1
        
        if self.mask[idx] == 1:
            self.mask[idx] = 0
            self.counts -= 1
        
    def flip(self) -> None:
        self.hasFlip = not self.hasFlip
        
    def all(self) -> bool:
        if not self.hasFlip:
            return self.counts == self.n
        else:
            return self.counts == 0

    def one(self) -> bool:
        if not self.hasFlip:
            return self.counts > 0
        else:
            return self.n - self.counts > 0

    def count(self) -> int:
        if not self.hasFlip:
            return self.counts
        else:
            return self.n - self.counts

    def toString(self) -> str:
        res = []
        
        for x in self.mask:
            if self.hasFlip:
                res.append("1" if x == 0 else "0")
            else:
                res.append(str(x))
        
        return "".join(res)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()