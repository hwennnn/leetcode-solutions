---
id: h-index-ii
title: H-Index II
description: Problem Description and Solution for H-Index II
sidebar_label: 275. H-Index II
sidebar_position: 275
---

# [275. H-Index II](https://leetcode.com/problems/h-index-ii/)

```py title=h-index-ii.py
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        
        n = len(citations)
        
        beg, end = 0, n - 1
        
        while beg <= end:
            mid = (beg + end)//2
            
            if mid + citations[mid] >= n:
                end = mid - 1
            else:
                beg = mid + 1             
                
        return n - beg
```


