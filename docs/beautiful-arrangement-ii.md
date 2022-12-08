---
id: beautiful-arrangement-ii
title: Beautiful Arrangement II
description: Problem Description and Solution for Beautiful Arrangement II
sidebar_label: 667. Beautiful Arrangement II
sidebar_position: 667
---

# [667. Beautiful Arrangement II](https://leetcode.com/problems/beautiful-arrangement-ii/)

```py title=beautiful-arrangement-ii.py
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        
        i, j = 1, n
        
        for _ in range(n):
            if k % 2 == 0:
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1
            
            if k > 1:
                k -= 1
        
        return res
```


