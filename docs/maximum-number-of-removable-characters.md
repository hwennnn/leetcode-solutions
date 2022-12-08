---
id: maximum-number-of-removable-characters
title: Maximum Number of Removable Characters
description: Problem Description and Solution for Maximum Number of Removable Characters
sidebar_label: 1898. Maximum Number of Removable Characters
sidebar_position: 1898
---

# [1898. Maximum Number of Removable Characters](https://leetcode.com/problems/maximum-number-of-removable-characters/)

```py title=maximum-number-of-removable-characters.py
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n = len(s)
        pn = len(p)
        rn = len(removable)
        
        def good(x):
            x = rn - x
            sset = set(removable[:x])
            j = 0
            
            for i, x in enumerate(s):
                if x == p[j] and i not in sset:
                    j += 1
                
                if j == pn: return True
            
            return False
            
        left, right = 0, rn
        while left < right:
            mid = (left + right) // 2

            if good(mid):
                right = mid
            else:
                left = mid + 1

        return rn - left
        
                
```


