class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.perms = []
        self.n = len(characters)
        self.k = combinationLength
        self.index = 0
        
        def go(i, curr):
            if len(curr) == self.k:
                self.perms.append(curr)
            
            if i == self.n:
                return

            for j in range(i, self.n):
                go(j + 1, curr + characters[j])

        go(0, '')

    def next(self) -> str:
        res = self.perms[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        return self.index < len(self.perms)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()