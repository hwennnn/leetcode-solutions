---
id: destroying-asteroids
title: Destroying Asteroids
description: Problem Description and Solution for Destroying Asteroids
sidebar_label: 2126. Destroying Asteroids
sidebar_position: 2126
---

# [2126. Destroying Asteroids](https://leetcode.com/problems/destroying-asteroids/)

```py title=destroying-asteroids.py
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for x in asteroids:
            if mass >= x:
                mass += x
            else:
                return False
        
        return True
```


