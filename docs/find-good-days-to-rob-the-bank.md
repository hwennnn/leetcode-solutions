---
id: find-good-days-to-rob-the-bank
title: Find Good Days to Rob the Bank
description: Problem Description and Solution for Find Good Days to Rob the Bank
sidebar_label: 2100. Find Good Days to Rob the Bank
sidebar_position: 2100
---

# [2100. Find Good Days to Rob the Bank](https://leetcode.com/problems/find-good-days-to-rob-the-bank/)

```py title=find-good-days-to-rob-the-bank.py
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0: return list(range(n))
        if n <= time * 2: return []
        
        res = []
        inc = [1] * n
        dec = [1] * n
        
        for i, x in enumerate(security):
            if i == 0: continue
            
            if x <= security[i - 1]:
                inc[i] += inc[i - 1]
        
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                dec[i] += dec[i + 1]
                    
        for i, x in enumerate(security[time: n - time], time):
            if x <= security[i - 1] and inc[i - 1] >= time and x <= security[i + 1] and dec[i + 1] >= time:
                res.append(i)
            
                
        
        return res
```


