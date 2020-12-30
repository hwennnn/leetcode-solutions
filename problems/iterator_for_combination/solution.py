class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.c = characters
        self.n = len(characters)
        self.p = self.generateCombinations(combinationLength, self.n)
        self.idx = len(self.p) - 1
        

    def next(self) -> str:
        res = []
        
        for i in range(self.n):
            if self.p[self.idx][i] != "0":
                res.append(self.c[i])
                
        self.idx -= 1
        
        return "".join(res)

    def hasNext(self) -> bool:
        return self.idx >= 0
    
    def generateCombinations(self, l, n):
        m = int("1"*n, 2)
        
        res = []
        for i in range(m+1):
            b = bin(i)[2:]
            if b.count("1") == l:
                res.append(b.zfill(n))
        
        return res
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()