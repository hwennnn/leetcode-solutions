---
id: odd-even-jump
title: Odd Even Jump
description: Problem Description and Solution for Odd Even Jump
sidebar_label: 975. Odd Even Jump
sidebar_position: 975
---

# [975. Odd Even Jump](https://leetcode.com/problems/odd-even-jump/)

```py title=odd-even-jump.py
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_higher, next_lower = [0] * n, [0] * n
        
        stack = []
        for x, i in sorted((x, i) for i, x in enumerate(arr)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            
            stack.append(i)
        
        stack = []
        for x, i in sorted((-x, i) for i, x in enumerate(arr)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            
            stack.append(i)
        
        odd, even = [0] * n, [0] * n
        odd[-1] = even[-1] = 1
        
        for i in range(n - 2, -1, -1):
            odd[i] = even[next_higher[i]]
            even[i] = odd[next_lower[i]]
        
        return sum(odd)
            
```


