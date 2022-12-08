---
id: minimum-time-to-remove-all-cars-containing-illegal-goods
title: Minimum Time to Remove All Cars Containing Illegal Goods
description: Problem Description and Solution for Minimum Time to Remove All Cars Containing Illegal Goods
sidebar_label: 2167. Minimum Time to Remove All Cars Containing Illegal Goods
sidebar_position: 2167
---

# [2167. Minimum Time to Remove All Cars Containing Illegal Goods](https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/)

```py title=minimum-time-to-remove-all-cars-containing-illegal-goods.py
class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        
        if n == 1: return 1 if s == "1" else 0
        
        left, right = [], []
        
        curr = 0
        for x in s:
            if x == "1":
                curr += 1
            else:
                curr -= 1
            
            left.append(curr)
        
        curr = 0
        for x in s[::-1]:
            if x == "1":
                curr += 1
            else:
                curr -= 1
            
            right.append(curr)
        right.reverse()
        
        leftMax, leftCurr = [left[0]], left[0]
        for i in range(1, n):
            leftCurr = max(leftCurr, left[i])
            leftMax.append(leftCurr)
        
        rightMax, rightCurr = [right[-1]], right[-1]
        for i in range(n - 2, -1, -1):
            rightCurr = max(rightCurr, right[i])
            rightMax.append(rightCurr)
        rightMax.reverse()
        
        total = 2 * s.count("1")
        save = 0
        
        for i in range(n - 1):
            save = max(save, max(0, leftMax[i]) + max(0, rightMax[i + 1]))
        
        return total - save
```


