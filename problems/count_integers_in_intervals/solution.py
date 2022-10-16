from sortedcontainers import SortedList

class CountIntervals:

    def __init__(self):
        self.sl = SortedList()
        self.res = 0
        
    def add(self, left: int, right: int) -> None:
        def overlap(l1, r1, l2, r2):
            lo = max(l1, l2)
            hi = min(r1, r2)
            
            return hi >= lo

        i = j = self.sl.bisect_left((left, -1))
        
        if i - 1 >= 0 and self.sl[i - 1][1] >= left:
            i -= 1
        
        while j < len(self.sl) and overlap(left, right, *self.sl[j]):
            j += 1

        for k in range(j - 1, i - 1, -1):
            L, R = self.sl[k]
            left = min(left, L)
            right = max(right, R)
            self.res -= R - L + 1
            del self.sl[k]
        
        self.res += right - left + 1
        self.sl.add((left, right))

    def count(self) -> int:
        return self.res
        


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()