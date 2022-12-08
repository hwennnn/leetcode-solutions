---
id: seat-reservation-manager
title: Seat Reservation Manager
description: Problem Description and Solution for Seat Reservation Manager
sidebar_label: 1845. Seat Reservation Manager
sidebar_position: 1845
---

# [1845. Seat Reservation Manager](https://leetcode.com/problems/seat-reservation-manager/)

```py title=seat-reservation-manager.py
class SeatManager:

    def __init__(self, n: int):
        self.heap = list(range(1, n + 1))

    def reserve(self) -> int:
        x = heapq.heappop(self.heap)
        
        return x

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
```


