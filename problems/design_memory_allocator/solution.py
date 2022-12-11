class Allocator:

    def __init__(self, n: int):
        self.N = n
        self.mp = defaultdict(list)
        self.A = [0] * self.N

    def allocate(self, size: int, mID: int) -> int:
        curr = 0
        
        for i in range(self.N):
            if self.A[i] != 0:
                curr = 0
            else:
                curr += 1
                
                if curr == size:
                    start = i - size + 1

                    for k in range(start, start + size):
                        self.mp[mID].append(k)
                        self.A[k] = 1

                    return start
        
        return -1

    def free(self, mID: int) -> int:
        count = 0
        
        for index in self.mp[mID]:
            count += 1
            self.A[index] = 0
        
        self.mp[mID].clear()
        
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)