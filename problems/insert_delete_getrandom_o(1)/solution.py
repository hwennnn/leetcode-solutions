class RandomizedSet:

    def __init__(self):
        self.mp = {}
        self.A = []

    def insert(self, val: int) -> bool:
        if val in self.mp: return False
        self.A.append(val)
        self.mp[val] = len(self.A) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp: return False
        last = self.A[-1]
        self.mp[last] = self.mp[val]
        self.A[self.mp[val]] = last
        self.A.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.A)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()