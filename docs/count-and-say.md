---
id: count-and-say
title: Count and Say
description: Problem Description and Solution for Count and Say
sidebar_label: 38. Count and Say
sidebar_position: 38
---

# [38. Count and Say](https://leetcode.com/problems/count-and-say/)

```py title=count-and-say.py
class Solution:
    def countAndSay(self, n: int) -> str:
        
        @cache
        def go(i):
            if i == 1: return "1"
            
            prev = go(i - 1)
            res = ""
            
            for k, g in groupby(prev):
                res += str(len(list(g))) + k
            
            return res
    
        return go(n)
```


