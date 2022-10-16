class RandomizedCollection:

    def __init__(self):
        self.mp = collections.defaultdict(list)
        self.A = []
        
    def insert(self, val: int) -> bool:
        isExist = len(self.mp[val]) == 0
        
        self.mp[val].append(len(self.A))
        self.A.append((val, len(self.mp[val]) - 1))
        
        return isExist

    def remove(self, val: int) -> bool:
        if len(self.mp[val]) == 0: return False
        
        last = self.A[-1]
        self.mp[last[0]][last[1]] = self.mp[val][-1]
        self.A[self.mp[val].pop()] = last
        self.A.pop()
        
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.A)[0]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()