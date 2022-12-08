---
id: minimum-number-of-taps-to-open-to-water-a-garden
title: Minimum Number of Taps to Open to Water a Garden
description: Problem Description and Solution for Minimum Number of Taps to Open to Water a Garden
sidebar_label: 1326. Minimum Number of Taps to Open to Water a Garden
sidebar_position: 1326
---

# [1326. Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/)

```py title=minimum-number-of-taps-to-open-to-water-a-garden.py
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        A = [0] * (n + 1)
        
        for i, x in enumerate(ranges):
            if x == 0: continue
            
            left = max(i - x, 0)
            A[left] = max(A[left], i + x)
        
        jumps = currStep = currFarthest = i = 0
        
        while i < len(A) and currStep < n:
            jumps += 1
            
            while i < len(A) and i <= currStep:
                currFarthest = max(currFarthest, A[i])
                i += 1
            
            if currStep == currFarthest: return -1
            
            currStep = currFarthest
        
        return jumps
```


