---
id: count-collisions-on-a-road
title: Count Collisions on a Road
description: Problem Description and Solution for Count Collisions on a Road
sidebar_label: 2211. Count Collisions on a Road
sidebar_position: 2211
---

# [2211. Count Collisions on a Road](https://leetcode.com/problems/count-collisions-on-a-road/)

```py title=count-collisions-on-a-road.py
class Solution:
    def countCollisions(self, A: str) -> int:
        n = len(A)
        res = 0
        stack = []
        
        for i, x in enumerate(A):
            stack.append(x)
            
            while len(stack) >= 2:
                if stack[-2] == "R" and stack[-1] == "L":
                    res += 2
                    stack.pop()
                    stack.pop()
                    stack.append("S")
                elif stack[-2] == "S" and stack[-1] == "L":
                    res += 1
                    stack.pop()
                    stack.pop()
                    stack.append("S")
                elif stack[-2] == "R" and stack[-1] == "S":
                    res += 1
                    stack.pop()
                    stack.pop()
                    stack.append("S")
                else:
                    break
        
        return res
```


