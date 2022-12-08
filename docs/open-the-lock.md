---
id: open-the-lock
title: Open the Lock
description: Problem Description and Solution for Open the Lock
sidebar_label: 752. Open the Lock
sidebar_position: 752
---

# [752. Open the Lock](https://leetcode.com/problems/open-the-lock/)

```py title=open-the-lock.py
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(["0000"])
        queue = deque([("0000", 0)])
        deadends = set(deadends)
        if "0000" in deadends: return -1
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == target: return steps
            
            ss = set()
            
            for i in range(4):
                digit = (int(curr[i]) + 1) % 10
                s = curr[:i] + str(digit) + curr[i + 1:]
                ss.add(s)
                
                digit = (int(curr[i]) - 1) % 10
                s = curr[:i] + str(digit) + curr[i + 1:]
                ss.add(s)
            
            for word in ss:
                if word not in deadends and word not in visited:
                    visited.add(word)
                    queue.append((word, steps + 1))
        
        return -1
```


