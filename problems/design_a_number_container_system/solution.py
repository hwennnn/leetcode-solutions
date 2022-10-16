from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.A = {}
        self.sl = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.A:
            prevNumber = self.A[index]
            self.sl[prevNumber].remove(index)
            
        self.A[index] = number
        self.sl[number].add(index)
        

    def find(self, number: int) -> int:
        s = self.sl[number]
        
        if not s: return -1
        
        return s[0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)