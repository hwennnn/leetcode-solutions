---
id: kth-smallest-number-in-multiplication-table
title: Kth Smallest Number in Multiplication Table
description: Problem Description and Solution for Kth Smallest Number in Multiplication Table
sidebar_label: 668. Kth Smallest Number in Multiplication Table
sidebar_position: 668
---

# [668. Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/)

```py title=kth-smallest-number-in-multiplication-table.py
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def enough(x):
            count = 0
            for r in range(1, m+1):
                count += min(x // r, n)
            
            return count >= k
        
        left, right = 1, m*n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if enough(mid):
                right = mid
            else:
                left = mid + 1
            
        return left
```


