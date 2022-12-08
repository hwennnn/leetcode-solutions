---
id: asteroid-collision
title: Asteroid Collision
description: Problem Description and Solution for Asteroid Collision
sidebar_label: 735. Asteroid Collision
sidebar_position: 735
---

# [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)

```py title=asteroid-collision.py
class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        n = len(A)
        stack = []
        
        for x in A:
            while stack and (x < 0 and stack[-1] > 0):
                if stack[-1] == -x:
                    stack.pop()
                    break
                    
                elif stack[-1] > -x:
                    break
                
                else:
                    stack.pop()
            
            else:
                stack.append(x)
        
        return stack
                
```


