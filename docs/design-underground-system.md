---
id: design-underground-system
title: Design Underground System
description: Problem Description and Solution for Design Underground System
sidebar_label: 1396. Design Underground System
sidebar_position: 1396
---

# [1396. Design Underground System](https://leetcode.com/problems/design-underground-system/)

```py title=design-underground-system.py
class UndergroundSystem:

    def __init__(self):
        self.checkIns = {}
        self.count = defaultdict(int)
        self.time = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, t1 = self.checkIns.pop(id)
        self.count[(start, stationName)] += 1
        self.time[(start, stationName)] += t - t1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.time[(startStation, endStation)] / self.count[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
```


