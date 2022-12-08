---
id: maximum-good-people-based-on-statements
title: Maximum Good People Based on Statements
description: Problem Description and Solution for Maximum Good People Based on Statements
sidebar_label: 2151. Maximum Good People Based on Statements
sidebar_position: 2151
---

# [2151. Maximum Good People Based on Statements](https://leetcode.com/problems/maximum-good-people-based-on-statements/)

```py title=maximum-good-people-based-on-statements.py
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        res = 0
        
        for mask in range(1, 1 << n):
            count = 0
            valid = True
            
            for j in range(n):
                if mask & (1 << j) > 0:
                    count += 1
                    
                    for k in range(n):
                        if statements[j][k] == 1 and mask & (1 << k) == 0:
                            valid = False
                            break
                        elif statements[j][k] == 0 and mask & (1 << k) > 0:
                            valid = False
                            break
            
            if valid:
                res = max(res, count)
        
        return res
        
```


