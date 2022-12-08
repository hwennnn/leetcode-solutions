---
id: calculate-digit-sum-of-a-string
title: Calculate Digit Sum of a String
description: Problem Description and Solution for Calculate Digit Sum of a String
sidebar_label: 2243. Calculate Digit Sum of a String
sidebar_position: 2243
---

# [2243. Calculate Digit Sum of a String](https://leetcode.com/problems/calculate-digit-sum-of-a-string/)

```py title=calculate-digit-sum-of-a-string.py
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            i = 0
            n = len(s)
            curr = 0
            temp = []
            count = 0
            
            while i < n:
                count += 1
                curr += int(s[i])
                
                if count == k or i == n - 1:
                    temp.append(str(curr))        
                    curr = 0
                    count = 0
                    
                i += 1
            
            s = "".join(temp)
        
        return s
```


