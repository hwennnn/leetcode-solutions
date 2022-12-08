---
id: next-greater-element-iii
title: Next Greater Element III
description: Problem Description and Solution for Next Greater Element III
sidebar_label: 556. Next Greater Element III
sidebar_position: 556
---

# [556. Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/)

```py title=next-greater-element-iii.py
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        
        i = len(s) - 2
        while i >= 0 and s[i] >= s[i+1]:
            i -= 1
        
        if i < 0: return -1
        
        j = len(s) - 1
        while s[j] <= s[i]:
            j -= 1
        
        s[i],s[j] = s[j],s[i]
        
        s[i+1:] = reversed(s[i+1:])
        
        res = int("".join(s))
        
        return res if res < (1 << 31) else -1 
    
```


