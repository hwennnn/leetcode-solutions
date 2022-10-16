from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.sl = SortedList([(float('-inf'), float('-inf')), (float('inf'), float('inf'))])
        
    def book(self, start: int, end: int) -> bool:
        index = self.sl.bisect_left((start, end))
        
        if start < self.sl[index - 1][1] or end > self.sl[index][0]: return False

        self.sl.add((start, end))    
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)