from sortedcontainers import SortedList

class SortedListWithSum:
    def __init__(self):
        self.items = SortedList()
        self.total = 0
        
    def add(self, item):
        self.total += item
        self.items.add(item)
        
    def remove(self, item):
        self.total -= item
        self.items.remove(item)

class MKAverage:
    
    def __init__(self, m: int, k: int):
        # inside
        self.m = m
        # smallest
        self.k = k
        
        self.buffer = collections.deque()
        self.left = SortedListWithSum()
        self.mid = SortedListWithSum()
        self.right = SortedListWithSum()

    def addElement(self, num: int) -> None:
        self.buffer.append(num)
        
        if len(self.buffer) > self.m:
            r = self.buffer.popleft()
            
            if r in self.right.items:
                self.right.remove(r)
            elif r in self.mid.items:
                self.mid.remove(r)
                
                small = self.right.items[0]
                self.right.remove(small)
                self.mid.add(small)
            else:
                self.left.remove(r)
                
                small = self.mid.items[0]
                self.mid.remove(small)
                self.left.add(small)
                
                small = self.right.items[0]
                self.right.remove(small)
                self.mid.add(small)
        
        self.left.add(num)
        if len(self.left.items) > self.k:
            big = self.left.items[-1]
            self.left.remove(big)
            
            self.mid.add(big)
            if len(self.mid.items) > self.m - self.k - self.k:
                big = self.mid.items[-1]
                self.mid.remove(big)
                self.right.add(big)
        #print(self.left.items, self.mid.items,  self.right.items, self.mid.total, self.m, self.k)        

    def calculateMKAverage(self) -> int:
        if len(self.buffer) >= self.m:
            #print(self.left.items, self.mid.items,  self.right.items, self.mid.total, self.m, self.k)
            return int(self.mid.total / (self.m - self.k - self.k))
        else:
            return -1
        
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
