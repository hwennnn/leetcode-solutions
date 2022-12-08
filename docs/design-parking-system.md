---
id: design-parking-system
title: Design Parking System
description: Problem Description and Solution for Design Parking System
sidebar_label: 1603. Design Parking System
sidebar_position: 1603
---

# [1603. Design Parking System](https://leetcode.com/problems/design-parking-system/)

```py title=design-parking-system.py
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.A = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        carType -= 1
        if self.A[carType] > 0:
            self.A[carType] -= 1
            return True
        
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
```


