---
id: my-calendar-i
title: My Calendar I
description: Problem Description and Solution for My Calendar I
sidebar_label: 729. My Calendar I
sidebar_position: 729
---

# [729. My Calendar I](https://leetcode.com/problems/my-calendar-i/)

```py title=my-calendar-i.py
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
```


